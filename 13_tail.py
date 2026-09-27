import pandas as pd

df = pd.read_csv("students.csv")

print("Last five records:")
print(df.tail())
