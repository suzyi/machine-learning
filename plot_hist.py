import matplotlib.pyplot as plt


def plot_error_hist(errors_train, errors_test_ok, errors_test_ng, fileName="hist.png"):
    """
    inputs:
        errors_train (list): A list float values.
        errors_test_ok (list): A list float values.
        errors_test_ng (list): A list float values.
    outputs:
        
    """
    thresh = 0.0216
    kwargs = dict(alpha=0.3, bins=100) # alpha controls transparency
    plt.hist(errors_train, **kwargs, color='r', label=f'train(ok, {len(errors_train)})')
    plt.hist(errors_test_ok, **kwargs, color='g', label=f'test(ok, {len(errors_test_ok)})')
    plt.hist([e for e in errors_test_ng if e<thresh], **kwargs, color='b', label=f'test(ng, {len(errors_test_ng)})')
#     plt.hist(sorted(errors_test_ng)[:60], **kwargs, color='b', label=f'test(ng, {len(errors_test_ng)})')
    plt.gca().set(xlabel='error', ylabel='count') # gca stands for "get current axes"
    plt.legend()
    plt.savefig(f"results/{fileName}")
    plt.close()