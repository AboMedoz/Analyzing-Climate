import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# https://github.com/MayumyCH/data-scientist-with-python-datacamp/blob/main/1.%20Courses/datasets/seattle_weather.csv
data = pd.read_csv('seattle_weather.csv')
print(data)

data.info()
print(data.isna().sum())
print(data.duplicated().sum())  # 0

# Visualising NaN Data
sns.heatmap(data.isna(), cmap='magma', cbar=False)
plt.title('Missing Data')
plt.show()

print(data.shape)
data = data.dropna()
print(data.shape)

# Seasonal Temperature over Time
plt.figure(figsize=(12, 6))
sns.lineplot(x=data['DATE'], y=data['MLY-TMIN-NORMAL'], label="Min Temp", color="blue")
sns.lineplot(x=data['DATE'], y=data['MLY-TMAX-NORMAL'], label="Max Temp", color="red")
plt.xlabel("Date")
plt.ylabel("Temperature (°F)")
plt.title("Seasonal Temperature Over Time")
plt.legend()
plt.show()


# Degree of the Days
# Using abs() due to Negative Values existing
plt.figure(figsize=(12, 6))
sns.lineplot(x=data['DATE'], y=data['MLY-CLDD-BASE50'].abs(), label="Cooling Degree Days (Base 50)")
sns.lineplot(x=data['DATE'], y=data['MLY-HTDD-BASE50'].abs(), label="Heating Degree Days (Base 50)")
plt.xlabel("Date")
plt.ylabel("Degree Days")
plt.title("Degree of Days Over Time")
plt.legend()
plt.show()


# Temperature Distribution
plt.figure(figsize=(10, 5))
plt.hist(data['MLY-TMIN-NORMAL'], bins=20, color='skyblue', edgecolor='black')
plt.title('Temperature Distribution')
plt.xlabel('Temperature')
plt.show()

