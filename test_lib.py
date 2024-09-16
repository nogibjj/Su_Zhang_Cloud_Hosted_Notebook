"""Test if functions in the calculator.py work normally"""

from mylib.calculator import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_max,
    grab_std,
    create_histogram,
)

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv"


def test_load_dataset():
    df = load_dataset(example_csv)
    assert df is not None
    assert df.shape == (17, 28)


def test_create_histogram():
    output_hist = create_histogram(load_dataset(example_csv), "alcohol_use")
    assert output_hist is None


def test_stats():
    """test that checks the data operations is working"""
    df = load_dataset(example_csv)
    mean_test = grab_mean(df, "alcohol_use")
    median_test = grab_median(df, "alcohol_use")
    std_test = grab_std(df, "alcohol_use")
    max_test = grab_max(df, "alcohol_use")
    describe_test = df.describe()
    assert describe_test.loc["mean", "alcohol_use"] == mean_test
    assert describe_test.loc["std", "alcohol_use"] == std_test
    assert describe_test.loc["50%", "alcohol_use"] == median_test
    assert describe_test.loc["max", "alcohol_use"] == max_test


if __name__ == "__main__":
    test_load_dataset()
    test_create_histogram()
    test_stats()
