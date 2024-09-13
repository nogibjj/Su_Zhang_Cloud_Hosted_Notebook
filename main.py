"""
Main cli or app entry point
"""

from mylib.calculator import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_max,
    grab_std,
    create_histogram,
)


def calculator_describe():
    c = load_dataset()
    return c.describe()


def save_to_md():
    with open("test.md", "a") as file:
        file.write("# Histogram")
        file.write("![Figure](figure.png)")


if __name__ == "__main__":
    print(calculator_describe())
    print(grab_mean(load_dataset(), "alcohol_use"))
    create_histogram(load_dataset(), "alcohol_use")
    print(grab_median(load_dataset(), "alcohol_use"))
    print(grab_std(load_dataset(), "alcohol_use"))
    print(grab_max(load_dataset(), "alcohol_use"))
    save_to_md()
