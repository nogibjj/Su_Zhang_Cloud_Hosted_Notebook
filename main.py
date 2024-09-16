"""
Main file to apply the functions defined in calculator.py
Get statistics output from specific data input
"""

from mylib.calculator import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_max,
    grab_std,
    create_histogram,
    create_scatter,
)

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv"


def calculator_describe(dataset):
    c = load_dataset(dataset)
    return c.describe()


def save_to_md():
    with open("druguse_summary.md", "a") as file:
        file.write("# Histogram of Alcohol Use")
        file.write("![Figure](Histogram.png)")
        file.write("# Scatterplots of Alcohol, Marijuana, Cocaine, Crack Use by Age")
        file.write("![Figure](Scatterplot.png)")


if __name__ == "__main__":
    print(calculator_describe(example_csv))
    print(
        "The mean of alcohol use is {:.2f}".format(
            grab_mean(load_dataset(example_csv), "alcohol_use")
        )
    )
    print(
        "The median of alcohol use is {:.2f}".format(
            grab_median(load_dataset(example_csv), "alcohol_use")
        )
    )
    print(
        "The standard deviation of alcohol use is {:.2f}".format(
            grab_std(load_dataset(example_csv), "alcohol_use")
        )
    )
    print(
        "The maximum of alcohol use is {:.2f}".format(
            grab_max(load_dataset(example_csv), "alcohol_use")
        )
    )
    create_histogram(load_dataset(example_csv), "alcohol_use")
    create_scatter(
        load_dataset(example_csv),
        [
            "alcohol_use",
            "marijuana_use",
            "cocaine_use",
            "crack_use",
        ],
    )
    save_to_md()
