import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("20260430-RTT-April-2026-full-extract.csv")

df["Total All"] = pd.to_numeric(df["Total All"], errors="coerce")

df = df[df["Treatment Function Name"] != "Total"]

df = df.dropna(subset=["Provider Org Name", "Treatment Function Name", "Total All"])

top_providers = (
    df.groupby("Provider Org Name")["Total All"]
      .sum()
      .nlargest(10)
      .index
)

top_departments = (
    df.groupby("Treatment Function Name")["Total All"]
      .sum()
      .nlargest(10)
      .index
)

heat_df = df[
    (df["Provider Org Name"].isin(top_providers)) &
    (df["Treatment Function Name"].isin(top_departments))
]

heatmap_data = heat_df.pivot_table(
    index="Provider Org Name",
    columns="Treatment Function Name",
    values="Total All",
    aggfunc="sum",
    fill_value=0
)

plt.figure(figsize=(18,8))

sns.heatmap(
    heatmap_data,
    cmap="YlOrRd",
    annot=True,
    fmt=".0f",
    linewidths=0.5
)

plt.title("NHS Waiting List Heatmap")
plt.xlabel("Treatment Function")
plt.ylabel("NHS Provider")

plt.tight_layout()

plt.savefig("waiting_heatmap.png", dpi=300)

plt.show()