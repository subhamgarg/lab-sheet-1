import pandas as pd

df = pd.read_csv("students.csv")

print("Sorted by Marks in descending order:")
result = df.sort_values("Marks", ascending=False)
print(result)

print("\nSorted by City and Marks:")
result2 = df.sort_values(["City", "Marks"])
print(result2)
