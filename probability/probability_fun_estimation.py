
# http://seaborn.pydata.org/generated/seaborn.distplot.html#seaborn.distplot
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
# estimate data density function with distribution
# visualizing  univariate distribution

def density_est(data,fitfun):
    sns.set(color_codes=True)
    x = np.random.normal(loc=2,scale=12,size=100)
    params = sns.distplot(x, fit=stats.norm)
    plt.show()
    return params