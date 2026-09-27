import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.scatter(df["Age"], df["Marks"])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks")
plt.grid(True)
plt.show()
