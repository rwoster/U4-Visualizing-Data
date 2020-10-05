import pandas as pd 

def main():
    msrp_df = pd.read_csv("msrp.csv")
    print(msrp_df)
    new_row = pd.Series(["chevy corvette", 75, 2212], index=["CarName", "ModelYear", "MSRP"])
    msrp_df = msrp_df.append(new_row, ignore_index=True)
    print(msrp_df)
    modelyear_counts_ser = msrp_df["ModelYear"].value_counts()
    print(modelyear_counts_ser)

main()