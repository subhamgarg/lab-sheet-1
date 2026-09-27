import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()
