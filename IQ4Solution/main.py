import pandas as pd

df = pd.read_csv("input.csv")
print(df.iloc[1])
# OR
#print(df.loc[1]) # ok because index is default row numbers
print(df["num_credits"])
#df.iloc[0, 2] = 0.0
# OR
df.loc[0, "gpa"] = 0.0
# OR
#df = df.replace("NA", 0.0)
df.to_csv("output.csv")
