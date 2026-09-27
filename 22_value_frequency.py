import pandas as pd

df = pd.read_csv("students.csv")

print("Frequency of each city:")
print(df["City"].value_counts())
