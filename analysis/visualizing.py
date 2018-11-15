import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
data=pd.read_csv('Workbook.csv')
print(data)
sns.pairplot(data)
plt.show()