import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show first rows
print(df.head())
# Remove missing values
df = df.dropna()

# Show columns
print(df.columns)
print("\nMost Common Genres:")

print(df["listed_in"].value_counts().head(10))
print("\nTop Countries:")

print(df["country"].value_counts().head(10))
print("\nRelease Years:")

print(df["release_year"].value_counts().head(10))
top_genres = df["listed_in"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_genres.plot(kind="bar")
plt.title("Top Netflix Genres")
plt.show()
top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind="bar")
plt.title("Top Netflix Countries")
plt.show()
