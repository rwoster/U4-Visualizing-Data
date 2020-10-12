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

def line_chart_example(x, y, y2, filename):
    # x, y could be 1D lists, 
    # numpy arrays, pandas Series
    plt.plot(x, y, label="Squared") 
    plt.plot(x, y2, label="Cubed", color="red", lw=5)

    # beautify our chart!!
    plt.title("CPSC 222 First Chart :)")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)
    plt.legend() # show a legend

    # need to "show()" the figure
    # or save the figure to a file
    # PNG, PDF, JPG, ...
    #plt.show() 
    plt.savefig(filename)

def scatter_chart_example(x, y, filename):
    plt.figure() # creates a new "current" figure
    plt.scatter(x, y, s=500, marker="x", color="green")
    plt.savefig(filename)

def bar_chart_example(x, y, filename):
    plt.figure() # creates a new "current" figure
    plt.bar(x, y)
    plt.savefig(filename)

def pie_chart_example(x, y, filename):
    plt.figure() # creates a new "current" figure
    plt.pie(y, labels=x, autopct="%1.2f%%")
    plt.savefig(filename)

def histogram_chart_example(x, filename):
    plt.figure() # creates a new "current" figure
    plt.hist(x, bins=30, facecolor="green", edgecolor="black")
    # let's add an annotation!! this supports data vis goal #3
    plt.annotate("mean: %.2f" %(np.mean(x)), xy=(105.0, 85.0))
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
    y2 = []
    for val in x:
        y.append(val ** 2)
        y2.append(val ** 3)
    line_chart_example(x, y, y2, "line_example.png") # call

    scatter_chart_example(x, y, "scatter_example.png")
    bar_chart_example(x, y, "bar_example.png")
    # warmup 10/12
    bar_chart_example(modelyear_counts_ser.index, modelyear_counts_ser, "modelyear_bar.png")
    pie_chart_example(x, y, "pie_example.png")

    # histogram example
    # we need interesting data...
    # lets create 1000 samples from a "normal" distribution
    # (e.g. bell shaped)
    mean = 100.0
    stdev = 20.0
    num_samples = 1000
    random_data = np.random.normal(mean, stdev, num_samples)
    histogram_chart_example(random_data, "histogram_example.png")

main()