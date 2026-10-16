import pandas as pd
import numpy as np

# 1. Читання набору даних із URL та додавання заголовків
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(filename, names=headers)

# Заміна "?" на NaN
df.replace("?", np.nan, inplace=True)

# 2. Очищення основних числових стовпців 
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg_norm_loss)

avg_bore = df['bore'].astype('float').mean(axis=0)
df["bore"] = df["bore"].replace(np.nan, avg_bore)

# ВИКОНАННЯ ЗАВДАНЬ ІЗ ЛАБОРАТОРНОЇ

# Завдання 1. Замініть NaN у стовпці 'stroke' середнім значенням.
avg_stroke = df['stroke'].astype('float').mean(axis=0)
df["stroke"] = df["stroke"].replace(np.nan, avg_stroke)
print("1. NaN у стовпці 'stroke' замінено на середнє:", avg_stroke)

# Завдання 2. Нормалізуйте стовпець 'height'.
df['height'] = df['height'].astype('float')
df['height'] = df['height'] / df['height'].max()
print("2. Стовпець 'height' успішно нормалізовано.")

# Завдання 3.1. Створіть змінну індикатора для стовпця 'aspiration'
dummy_variable_1 = pd.get_dummies(df["aspiration"])

# Завдання 3.2. Об'єднайте новий фрейм даних із вихідним, а потім видаліть стовпець 'aspiration'.
df = pd.concat([df, dummy_variable_1], axis=1)
df.drop("aspiration", axis=1, inplace=True)
print("3. Стовпець 'aspiration' замінено на індикаторні змінні.")

# Спочатку переведемо потрібні колонки у float, де є чидлові дані
df[["bore", "stroke", "price", "peak-rpm", "horsepower"]] = df[["bore", "stroke", "price", "peak-rpm", "horsepower"]].astype("float")

# Завдання 4. Замініть усі NaN у всіх стовбцях середнім значенням.
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        mean_val = df[col].mean()
        df[col] = df[col].replace(np.nan, mean_val)

# Переводимо normalized-losses в int
df["normalized-losses"] = df["normalized-losses"].astype("int")

print("4. Усі залишки NaN у числових стовпцях замінено середніми значеннями.")

# Перевірка результату
print("\nРозмірність фінального датасету:", df.shape)
print(df.head())