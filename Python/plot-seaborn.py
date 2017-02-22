import numpy as np; np.random.seed(22)
import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt

x = np.linspace(0, 15, 31)
data = np.sin(x) + np.random.rand(10, 31) + np.random.randn(10, 1)
ax = sns.tsplot(data=data)
plt.show()

x = np.random.normal(size=100)
sns.distplot(x)
plt.show()

# y = input('Tekan Return')
