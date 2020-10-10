import pandas as pd

df = pd.read_csv("input.csv")
print(df.iloc[1])
print(df["num_credits"])
#df.iloc[0, 2] = 0.0
# OR
df.loc[0, "gpa"] = 0.0
df.to_csv("output.csv")