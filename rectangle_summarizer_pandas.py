# %% import pandas and read the csv file 
# modify the path if needed
import pandas as pd

df = pd.read_csv("DATA475_lab_rectangles_data.csv")
df["area"] = df["width"] * df["length"]


# %%
summary = [
    ("Total Count", df["area"].shape[0]),
    ("Total Area", df["area"].sum()),
    ("Total Area", df["area"].mean()),
    ("Total Area", df["area"].max()),
    ("Total Area", df["area"].min()),
]

for key, value in summary:
    print(f"{key}: {str(value)}")

# %%
pd.DataFrame(dict(summary), index=[0]).to_csv("summary.csv",index=False)

# %%
