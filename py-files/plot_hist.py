import matplotlib.pyplot as plt
import numpy as np

def plot_error_hist(temporature_Jul, temporature_Jan, fileName="hist.png"):
    """
    inputs:
        temporature_Jul (list): A list float values.
        temporature_Jan (list): A list float values.
    outputs:
        
    """
    thresh = 40.0
    kwargs = dict(alpha=0.3, bins=10) # alpha controls transparency
    plt.hist([e for e in temporature_Jul if e<thresh], **kwargs, color='r', label=f'temporature(July, {len(temporature_Jul)})')
    plt.hist(temporature_Jan, **kwargs, color='g', label=f'temporature(January, {len(temporature_Jan)})')
    plt.gca().set(xlabel='temporature(Celsius)', ylabel='count') # gca stands for "get current axes"
    plt.legend()
    plt.savefig(f"results/{fileName}")
    plt.close()
    
if __name__=="__main__":
    sigma = 1
    mu_Jul = 29
    temporature_Jul = np.random.normal(mu_Jul, sigma, 30).tolist()
    temporature_Jul.append(44) # append an outlier
    mu_Jan = 4
    temporature_Jan = np.random.normal(mu_Jan, sigma, 31).tolist()
    plot_error_hist(temporature_Jul, temporature_Jan, fileName="hist.png")
