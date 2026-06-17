import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("traffic_data.csv")

# Display first rows
print("First five rows:")
print(df.head())

# Calculate total visits
total_visits = df["Visits"].sum()
print("\nTotal Visits:", total_visits)

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    df["Visits"],
    labels=df["Source"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Website Traffic Sources")

plt.savefig("traffic_sources.png")
plt.show()
