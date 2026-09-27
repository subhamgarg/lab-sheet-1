import pandas as pd

df = pd.read_csv("students.csv")

print("Number of duplicate records:", df.duplicated().sum())

df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df)
