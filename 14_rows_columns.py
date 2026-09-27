import pandas as pd

df = pd.read_csv("students.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Shape:", df.shape)
