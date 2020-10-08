import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 


# EDA: exploratory data analysis
# goals of data vis
# 1. clearly and accurately represent data
# 2. be creative with the goal of increasing
# readability and understanding
# 3. label the units and points of interest

# jargon
# 2D visualizations are called charts
# plot: a chart of data points (scatter plot)
# graph: a chart of a math function (sine)

# matplotlib
# 3 ways to use matplotlib
# 1. using the pyplot module
# *there is always a "current" figure*
# 2. OOP interface
# 3. mix of the first two

def line_chart_example(x, y, filename):
    # x, y could be 1D lists, 
    # numpy arrays, pandas Series
    plt.plot(x, y) 

    # need to "show()" the figure
    # or save the figure to a file
    # PNG, PDF, JPG, ...
    #plt.show() 
    plt.savefig(filename)


def main():
    msrp_df = pd.read_csv("msrp.csv")
    print(msrp_df)
    new_row = pd.Series(["chevy corvette", 75, 2212], index=["CarName", "ModelYear", "MSRP"])
    msrp_df = msrp_df.append(new_row, ignore_index=True)
    print(msrp_df)
    modelyear_counts_ser = msrp_df["ModelYear"].value_counts()
    print(modelyear_counts_ser)

    # warm up task
    # split apply combine
    # split on ModelYear
    mean_msrp_group_ser = pd.Series()
    grouped_by_modelyear = msrp_df.groupby("ModelYear")
    for group_name, group_df in grouped_by_modelyear:
        # apply mean to the msrp column of each group
        mean_msrp_group = group_df["MSRP"].mean()
        #print(mean_msrp_group)
        # combine into a Series or DataFrame
        mean_msrp_group_ser[str(group_name)] = mean_msrp_group 
    print(mean_msrp_group_ser)

    # let's chart!!
    x = list(range(6)) # 0, 1, 2, 3, 4, 5
    y = []
    for val in x:
        y.append(val ** 2)
    line_chart_example(x, y, "line_example.pdf") # call

main()