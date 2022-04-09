import matplotlib.pyplot as plt
import numpy as np

def plot_error_hist(vec_1, vec_2, fileName="hist.png"):
    """
    inputs:
        vec_1 (list): A list float values.
        vec_2 (list): A list float values.
    outputs:
        
    """
    thresh = 40.0
    kwargs = dict(alpha=0.3, bins=30) # alpha controls transparency
    plt.hist([e for e in vec_1 if e<thresh], **kwargs, color='r', label=f'length of vec_1({len(vec_1)})')
    plt.hist(vec_2, **kwargs, color='g', label=f'length of vec_2({len(vec_2)})')
    plt.gca().set(xlabel='length', ylabel='count') # gca stands for "get current axes"
    plt.legend()
    plt.savefig(f"{fileName}")
    plt.close()
    
if __name__=="__main__":
    sigma = 1
    mu_1 = 29
    vec_1 = np.random.normal(mu_1, sigma, 30).tolist()
    vec_1.append(44) # append an outlier
    mu_2 = 4
    vec_2 = np.random.normal(mu_2, sigma, 31).tolist()
    plot_error_hist(vec_1, vec_2, fileName="hist.png")
