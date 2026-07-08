import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("etr.csv")
df.head()
df = pd.read_csv("etr.csv")
print(df.shape)
print(df.columns)
print(df.head())
import pandas as pd

df = pd.read_csv("etr.csv")
print("Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

df = df.dropna(axis=1, how="all")

print(df.shape)
print(df.head())

for i, col in enumerate(df.columns):
    print(i, ":", col)
    
import pandas as pd

df = pd.read_csv("etr.csv", header=None)

df.columns = [f"col_{i}" for i in range(df.shape[1])]
print(df.head())

df = df.rename(columns={
    "col_0": "provider_code",
    "col_1": "provider_name",
    "col_2": "region_code",
    "col_7": "city",
    "col_8": "postcode"
})

print(df.columns)

print(df.head())

print(df.shape)

print(df["city"].value_counts().head(10))

city_counts = df["city"].value_counts().head(10)

plt.figure(figsize=(10,5))
city_counts.plot(kind="bar")

plt.title("Top 10 Cities by Number of NHS Providers")
plt.xlabel("City")
plt.ylabel("Number of Providers")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.savefig("city_providers.png")
plt.show()

city_counts = df["city"].value_counts().head(10)

region_counts = df["region_code"].value_counts().head(10)

plt.figure(figsize=(8,5))
region_counts.plot(kind="bar", color="orange")

plt.title("Top Region Codes")
plt.xlabel("Region Code")
plt.ylabel("Number of Providers")

plt.tight_layout()
plt.savefig("region_providers.png")
plt.show()


hospital_counts = df["col_5"].value_counts().head(10)

plt.figure(figsize=(10,5))
hospital_counts.plot(kind="bar", color="green")

plt.title("Top Hospital Names")
plt.xlabel("Hospital")
plt.ylabel("Count")

plt.xticks(rotation=60)

plt.tight_layout()
plt.savefig("hospital_providers.png")
plt.show()

city_counts = df["city"].value_counts()

top5 = city_counts.head(5)
others = city_counts.iloc[5:].sum()

pie_data = top5.copy()
pie_data["Others"] = others

plt.figure(figsize=(7,7))
plt.pie(
    pie_data,
    labels=pie_data.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Share of NHS Providers Across Top 5 Cities")

plt.savefig("city_share_pie.png")
plt.show()


df = pd.read_csv("20260430-RTT-April-2026-full-extract.csv")

for col in df.columns:
    if ("Provider" in col
        or "Treatment" in col
        or "Function" in col
        or "Total" in col
        or "Organisation" in col
        or "Org" in col):
        print(col)
for col in df.columns:
    if "Name" in col:
        print(col)
for col in df.columns:
    if "Total" in col:
        print(col)
        
dept = (
    df.groupby("Treatment Function Name")["Total All"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))
dept.plot(kind="barh")

plt.title("Top 10 Treatment Functions by Waiting List")
plt.xlabel("Patients Waiting")
plt.ylabel("Department")

plt.tight_layout()
plt.savefig("top_departments.png")
plt.show()

provider = (
    df.groupby("Provider Org Name")["Total All"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))
provider.plot(kind="barh")

plt.title("Top 10 NHS Providers by Waiting List")
plt.xlabel("Patients Waiting")
plt.ylabel("Hospital Trust")

plt.tight_layout()
plt.show()

plt.savefig("graph_name.png", dpi=300, bbox_inches="tight")
plt.show()