import pandas as pd 

df = pd.read_csv("dogs.csv")

print(df)

grouped_by_size = df.groupby("size class")
ser = pd.Series(dtype=int)
for group_name, group_df in grouped_by_size:
    ser[group_name] = group_df["awards won"].sum()

print(ser)
ser.to_csv("total_awards.csv")

# OR
grouped_by_size =  df.groupby("size class")
ser = pd.Series(grouped_by_size["awards won"].sum())
print(ser)

