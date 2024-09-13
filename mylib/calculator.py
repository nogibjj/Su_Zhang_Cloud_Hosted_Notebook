"""library file"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv"
check = pd.read_csv(dataset)


def load_dataset():
    df = pd.read_csv(dataset)
    return df


def grab_mean(df, col):
    return df[col].mean()


def create_histogram(df, col):
    plt.hist(df[col], bins=20, edgecolor="white")
    plt.title("Histogram of {}".format(col))
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()


def grab_median(df, col):
    return df[col].median()


def grab_std(df, col):
    return df[col].std()


def grab_max(df, col):
    return df[col].max()
