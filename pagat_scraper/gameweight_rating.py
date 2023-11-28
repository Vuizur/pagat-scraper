# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load CSV table into dataframe
df = pd.read_csv("table.csv")

# Select two columns of interest
#x = df["GameWeight"]
#y = df["AvgRating"]

# Select columns where game weight is not 0.0
x = df[df["GameWeight"] != 0.0]["GameWeight"]
y = df[df["GameWeight"] != 0.0]["AvgRating"]

# Plot scatter plot
plt.scatter(x, y)
plt.xlabel("Game Weight")
plt.ylabel("Average Rating")
plt.title("Correlation between Game Weight and Average Rating")
plt.grid(True)
plt.show()

# Calculate correlation coefficient and p-value
corr, p = pearsonr(x, y)
print(f"The correlation coefficient is {corr:.2f} and the p-value is {p:.4f}")
