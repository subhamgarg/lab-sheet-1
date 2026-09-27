import pandas as pd

df = pd.read_csv("students.csv")

print("Column names:")
for column in df.columns:
    print(column)
