from sklearn.datasets import load_iris

iris = load_iris()

print("Iris data:")
print(iris.data)

print("\nTarget values:")
print(iris.target)

print("\nFeature names:")
print(iris.feature_names)

print("\nTarget names:")
print(iris.target_names)
