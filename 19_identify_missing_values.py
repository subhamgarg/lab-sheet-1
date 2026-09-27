import pandas as pd

df = pd.read_csv("students.csv")

print("Missing-value table:")
print(df.isnull())

print("\nDoes the dataset contain missing values?")
print(df.isnull().values.any())
