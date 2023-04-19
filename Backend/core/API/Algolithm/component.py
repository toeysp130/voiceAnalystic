from sklearn.mixture import *
import numpy as np

from .plot_component import plot_component
components_range = np.arange(1, 25)
def n_components(mfcc):
    print("Run n_components.py")
    # print(f"mfcc in n_components{mfcc}")
    model = [GaussianMixture(n, covariance_type='full', random_state=0).fit(mfcc)for n in components_range]
    #plot_component(model,mfcc,components_range)
    print("End n_components")
    return model
