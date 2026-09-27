from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

iris = load_iris(as_frame=True)
data = iris.frame.rename(columns={
    "petal length (cm)": "petal_length",
    "sepal length (cm)": "sepal_length",
})
data["species"] = data["target"].map(dict(enumerate(iris.target_names)))
data = data[["species", "petal_length", "sepal_length"]].dropna()
print(data.groupby("species")[["petal_length", "sepal_length"]].mean().round(2))

for species, group in data.groupby("species"):
    plt.scatter(group["petal_length"], group["sepal_length"], label=species)
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.show()

model = LinearRegression().fit(data[["petal_length"]], data["sepal_length"])
print("Intercept:", model.intercept_, "Slope:", model.coef_[0])
