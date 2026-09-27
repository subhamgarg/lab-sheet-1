import pandas as pd

df = pd.read_csv("students.csv")

df.drop("Gender", axis=1, inplace=True)

print("Dataset after deleting Gender column:")
print(df)
