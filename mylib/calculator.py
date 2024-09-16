"""library file that lists out all the necessary calculation functions"""

import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


def grab_mean(df, col):
    return df[col].mean()


def create_histogram(df, col):
    plt.hist(df[col], bins=20, edgecolor="white")
    plt.title("Histogram of {}".format(col))
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.savefig("figure.png")


def grab_median(df, col):
    return df[col].median()


def grab_std(df, col):
    return df[col].std()


def grab_max(df, col):
    return df[col].max()
