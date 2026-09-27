import pandas as pd

df = pd.read_csv("students.csv")

print("Missing values in each column:")
print(df.isnull().sum())
