"""
Test for main.py

"""

from main import calculator_describe

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv"


def test_describe():
    """test if describe function in main.py is actually working"""
    describe_test = calculator_describe(example_csv)
    assert (
        describe_test.loc["count", "alcohol_use"] == 17
    ), "The describe function did not work properly"
    assert "mean" in describe_test.index, "The describe function did not work properly"


if __name__ == "__main__":
    test_describe()
