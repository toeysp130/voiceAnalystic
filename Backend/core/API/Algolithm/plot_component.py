from matplotlib import pyplot as plt

def plot_component(models,mfcc,components_range):
    plt.figure(figsize=(15, 10))
    plt.plot(components_range, [m.bic(mfcc) for m in models], label='BIC')
    plt.plot(components_range, [m.aic(mfcc) for m in models], label='AIC')
    plt.legend(loc='best')
    plt.xlabel('GMM n_components for an audio file');
    #plt.show()