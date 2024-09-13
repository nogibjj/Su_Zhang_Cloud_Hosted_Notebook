"""
Main cli or app entry point
"""

from mylib.calculator import *


def calculator_describe():
    c = load_dataset()
    return c.describe()


def save_to_md():
    with open("test.md", "a") as file:
        file.write("test")


if __name__ == "__main__":
    print(calculator_describe())
    print(grab_mean(load_dataset(), "alcohol_use"))
    create_histogram(load_dataset(), "alcohol_use")
    print(grab_median(load_dataset(), "alcohol_use"))
    print(grab_std(load_dataset(), "alcohol_use"))
    save_to_md()
