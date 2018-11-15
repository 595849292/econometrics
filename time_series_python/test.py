import pandas as pd
import numpy as np
rng=pd.date_range('1/1/2011',periods=6,freq='H')
ts=pd.Series(np.random.randn(len(rng)),index=rng)
#converted=ts.asfreq('3H')
a=ts.resample('2H').sum().head(5)
print(a)