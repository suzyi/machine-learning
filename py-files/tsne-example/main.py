from sklearn.manifold import TSNE
from PIL import Image
import time
import torch
import os
import matplotlib.pyplot as plt
import torchvision.transforms as transforms


def tsne_fun(features_train_inDistribution, features_test_inDistribution, features_test_outOfDistribution):
    """
    inputs:
        features_train_inDistribution (torch.tensor):
        features_test_inDistribution (torch.tensor):
        features_test_outOfDistribution (torch.tensor):
    outputs:
        "tsne_result.png"
    """
    features = torch.cat([features_train_inDistribution, features_test_inDistribution, features_test_outOfDistribution], dim=0).numpy()
    n_components = 2
    
    start = time.time()
    features_2D = TSNE(n_components).fit_transform(features)
    end = time.time()
    
    print(f"TSNE used {(end-start)/60:.2f} minutes.")
    features_train_inDistribution_2D = features_2D[:len(features_train_inDistribution)]
    features_test_inDistribution_2D = features_2D[len(features_train_inDistribution):len(features_train_inDistribution)+len(features_test_inDistribution)]
    features_test_outOfDistribution_2D = features_2D[len(features_train_inDistribution)+len(features_test_inDistribution):]
    
    alpha = 0.3 # alpha controls transparency.
    fig = plt.figure(figsize=(6, 6))
    plt.scatter(features_train_inDistribution_2D[:, 0], features_train_inDistribution_2D[:, 1], marker="*", color="r", label=f"train (in distribution, {len(features_train_inDistribution_2D)})", alpha=alpha)
    plt.scatter(features_test_inDistribution_2D[:, 0], features_test_inDistribution_2D[:, 1], marker="*", color="g", label=f"test (in distribution, {len(features_test_inDistribution_2D)})", alpha=1)
    plt.scatter(features_test_outOfDistribution_2D[:, 0], features_test_outOfDistribution_2D[:, 1], marker="*", color="b", label=f"test (out of distribution, {len(features_test_outOfDistribution_2D)})", alpha=1)
    plt.legend(loc="upper right")
    plt.savefig("tsne_result.png")
    plt.close()
    
    
def get_features(path_to_img, transform):
    """
    inputs:
        path_to_img (string):
        transform (torchvision.transforms):
    outputs:
        features (torch.tensor):
    """
    features = list()
    for name in os.listdir(path_to_img):
        if name[-4:]==".png":
            img = Image.open(os.path.join(path_to_img, name))
            img = transform(img)
            features.append(img.reshape(1, -1))
    features = torch.cat(features, dim=0)
    return features
    
    
if __name__=="__main__":
    transform = transforms.Compose([transforms.Resize(size=(28, 28)),
                                    transforms.ToTensor(),
                                   ])
    features_train_inDistribution = get_features("imgs/train/0", transform)
    features_test_inDistribution = get_features("imgs/test/0", transform)
    features_test_outOfDistribution = get_features("imgs/test/1", transform)
    tsne_fun(features_train_inDistribution, features_test_inDistribution, features_test_outOfDistribution)