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
)

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv"


def calculator_describe(dataset):
    c = load_dataset(dataset)
    return c.describe()


def save_to_md():
    with open("test.md", "a") as file:
        file.write("# Histogram")
        file.write("![Figure](figure.png)")


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
    save_to_md()
