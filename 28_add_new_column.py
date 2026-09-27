import pandas as pd

df = pd.read_csv("students.csv")

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print(df)
