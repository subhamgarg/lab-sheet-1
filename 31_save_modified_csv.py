import pandas as pd

df = pd.read_csv("students.csv")

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

df.to_csv("modified_students.csv", index=False)

print("Modified dataset saved as modified_students.csv")
