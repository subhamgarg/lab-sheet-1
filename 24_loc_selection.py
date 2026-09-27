import pandas as pd

df = pd.read_csv("students.csv")

print("Rows 0 to 2, selected columns:")
print(df.loc[0:2, ["Name", "Marks"]])
