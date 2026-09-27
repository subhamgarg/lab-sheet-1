import pandas as pd

df = pd.read_csv("students.csv")

print("Unique cities:")
print(df["City"].unique())
