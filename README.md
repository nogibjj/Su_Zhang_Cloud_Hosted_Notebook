[![Format](https://github.com/nogibjj/Su_Zhang_Individual_Project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Su_Zhang_Individual_Project_1/actions/workflows/format.yml)

[![Install](https://github.com/nogibjj/Su_Zhang_Individual_Project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Su_Zhang_Individual_Project_1/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/Su_Zhang_Individual_Project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Su_Zhang_Individual_Project_1/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/Su_Zhang_Individual_Project_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Su_Zhang_Individual_Project_1/actions/workflows/test.yml)

# Su Zhang Individual Project #1 

# Youtube Link
[Youtube Link](https://www.youtube.com/@Su-Zhang)

# Purpose of the Project

This project aims to analyze a dataset on drug use, which includes the statistics on the sample population's alcolhol, marijuana, cocaine, and crack use grouped by age. This project primarily used Pandas and Matplotlib packages to analyze the distribution of alcohol use, summary statistics (mean, median, max, standard variation) of alcolhol, marijuana, cocaine, and crack use, as well as a scatterplot that illustrates the frequency of these drug uses of different age groups.

# Source of Data:

https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv

# Project Structure:

* `Makefile`: 
    - **install**: install `requirements.txt`
    - **test**: this project used **nbval** plugin to validate the jupyter notebook; runs **pytest** for both mylib and main; runs all test files matching the pattern test_*.py
    - **format**: format using black formatter
    - **lint**: this project used **Ruff** instead of pylint for testing, which makes the process faster
    - **generate_and_push**: this project added generate_and_push function to automatically add and push everything to github repo

* `requirements.txt`: specify pinned packages needed for this project, including **pandas, matplotlib, nbval, tabulate, jupyter**

* `my_lib`: includes library file `calculator.py` that contains all the functions defined to conduct statistics analysis towards the dataset

* `main.py`: calling out functions in calculator.py and execuate the statistics analysis 

* `test_main.py`: tests if the functions defined in main.py work normally

* `test_lib.py`: tests if the functions defined in calculator.py work properly

* `main.ipynb`: jupyter notebook that runs test against functions in library file (calculator.py) and shows the graphic output 

* `README.me`: project documentation that introduces purpose, data source, and structure

* `githubactions`: separates the commands into **four configuration files** - `install.yml`, `format.yml`, `test.yml`, `lint.yml`. In `test.yml`, I added the command of generate_and_push, which will push the edits to the github repo automatically after testing

* `devcontainer`: set up a development environment in Github Codespace, and Dockerfile to define the base environment

* `druguse_summary.md`: markdown file that saves the graphic output

* `Histogram.png`: histogram to illustrate the distribution of **alcohol use**

* `Scatterplot.png`: scatterplot to illustrate the frequency of **alcolhol, marijuana, cocaine, and crack use of different age groups**

* `Data_Summary.pdf`: Output pdf generated from Jupyter Notebook to showcase the analysis output

# Data Visualizations

![Histogram](Histogram.png)
![Scatterplot](Scatterplot.png)

# Template for the Project:
https://github.com/nogibjj/python-ruff-template
