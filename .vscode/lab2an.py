
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

columns = [
    "symboling", "normalized-losses", "make", "fuel-type",
    "aspiration", "num-of-doors", "body-style", "drive-wheels",
    "engine-location", "wheel-base", "length", "width",
    "height", "curb-weight", "engine-type", "num-of-cylinders",
    "engine-size", "fuel-system", "bore", "stroke",
    "compression-ratio", "horsepower", "peak-rpm",
    "city-mpg", "highway-mpg", "price"
]

df = pd.read_csv(url, names=columns, na_values="?")

print(df.head())


print("\nКореляція між параметрами:")

correlation = df[
    ["bore", "stroke", "compression-ratio", "horsepower"]
].corr()

print(correlation)

print("\nКореляція stroke та price:")

correlation = df["stroke"].corr(df["price"])

print(correlation)

import matplotlib.pyplot as plt

plt.scatter(df["stroke"], df["price"])

plt.xlabel("Stroke")
plt.ylabel("Price")
plt.title("Stroke vs Price")

plt.show()

print("\nСередня ціна за типом кузова:")

average_price = df.groupby("body-style")["price"].mean()

print(average_price)



from scipy.stats import pearsonr

data = df[["wheel-base", "price"]].dropna()

correlation, p_value = pearsonr(
    data["wheel-base"],
    data["price"]
)

print("\nPearson correlation (wheel-base та price):")
print("Correlation:", correlation)
print("P-value:", p_value)
