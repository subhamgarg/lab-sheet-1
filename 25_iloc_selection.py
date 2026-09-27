import pandas as pd

df = pd.read_csv("students.csv")

print("First three rows and first three columns:")
print(df.iloc[0:3, 0:3])
