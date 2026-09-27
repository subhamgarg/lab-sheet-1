import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 15, 25, 30, 35, 20, 15]

sns.histplot(data, kde=True)
plt.title("Basic Statistical Plot")
plt.xlabel("Value")
plt.show()
