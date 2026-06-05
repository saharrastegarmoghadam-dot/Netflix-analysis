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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

print(df.head())
df = df.dropna(subset=["director", "country", "release_year", "listed_in"])
print("\nTop 10 Directors:")

top_directors = df["director"].value_counts().head(10)
print(top_directors)
year_counts = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(year_counts.index, year_counts.values)
plt.title("Netflix Content Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()
type_counts = df["type"].value_counts()

plt.figure(figsize=(6,4))
type_counts.plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind="bar")
plt.title("Top Netflix Countries")
plt.show()
top_genres = df["listed_in"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_genres.plot(kind="bar")
plt.title("Top Netflix Genres")
plt.show()
print("\nAverage content per year:")
print(df["release_year"].value_counts().mean())