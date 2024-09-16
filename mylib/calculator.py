"""library file that lists out all the necessary calculation functions"""

import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


def grab_mean(df, col):
    return df[col].mean()


def create_histogram(df, col, jupyter_output=False):
    plt.hist(df[col], bins=20, edgecolor="white")
    plt.title("Histogram of {}".format(col))
    plt.xlabel(col)
    plt.ylabel("Frequency")
    if jupyter_output is False:
        plt.savefig("Histogram.png")
        plt.close()
    else:
        plt.show()


def grab_median(df, col):
    return df[col].median()


def grab_std(df, col):
    return df[col].std()


def grab_max(df, col):
    return df[col].max()


def create_scatter(df, columns, jupyter_output=False):
    colors = ["red", "green", "yellow", "blue"]
    for i, column in enumerate(columns):
        plt.scatter(df["age"], df[column], label=column, color=colors[i])
    plt.xlabel("Age")
    plt.xticks(rotation=45)
    plt.ylabel("Frequency")
    plt.title("Scatterplot of {}".format(", ".join(columns)))
    plt.legend()
    if jupyter_output is False:
        plt.savefig("Scatterplot.png")
        plt.close()
    else:
        plt.show()
