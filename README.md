# suraj_datalab

[![PyPI version](https://img.shields.io/pypi/v/suraj_datalab.svg)](https://pypi.org/project/suraj_datalab/)
[![License](https://img.shields.io/pypi/l/suraj_datalab.svg)](https://github.com/surajwate/suraj_datalab/blob/master/LICENSE)
[![Build Status](https://github.com/surajwate/suraj_datalab/actions/workflows/publish.yml/badge.svg)](https://github.com/surajwate/suraj_datalab/actions)

`suraj_datalab` is a Python package designed to streamline the process of analyzing and visualizing both categorical and numerical data. It provides easy-to-use functions to help you better understand your datasets.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Examples](#examples)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Features

- **Categorical Analysis**: Effortlessly analyze and visualize categorical data in relation to target variables.
- **Numerical Analysis**: Detect, analyze, and visualize outliers in numerical data.
- **Visualization**: Built-in support for generating insightful plots with minimal code.
- **Extensible**: Designed with flexibility in mind, allowing easy extension and integration with other data processing workflows.

## Installation

### Requirements

- Python 3.12 or higher
- [pandas](https://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](https://matplotlib.org/)

### Install via pip

```bash
pip install suraj_datalab
```

## Quickstart

Here’s how you can quickly get started with `suraj_datalab`:

```python
import pandas as pd
from suraj_datalab.analysis import analyze_categorical_feature, analyze_numerical_feature

# Sample DataFrame
data = {'Feature': ['A', 'B', 'A', 'B'], 'Transported': [True, False, True, False]}
df = pd.DataFrame(data)

# Categorical Analysis
result = analyze_categorical_feature(df, 'Feature')
print(result)

# Numerical Analysis
numeric_data = {'NumericFeature': [1, 2, 3, 4, 5], 'Transported': [True, False, True, False, True]}
df_numeric = pd.DataFrame(numeric_data)
outliers_df, summary_df = analyze_numerical_feature(df_numeric, 'NumericFeature')
print(outliers_df)
print(summary_df)
```

## Usage

`suraj_datalab` provides two primary functions:

- **`analyze_categorical_feature(df, feature, target)`**: Analyze a categorical feature in relation to a target variable.
- **`analyze_numerical_feature(df, feature_col, target_col)`**: Analyze a numerical feature and detect outliers.

## Examples

### Categorical Analysis

Analyze the distribution of a categorical feature and visualize it:

```python
result = analyze_categorical_feature(df, 'Feature')
print(result)
```

### Numerical Analysis

Detect and analyze outliers in numerical data:

```python
outliers_df, summary_df = analyze_numerical_feature(df_numeric, 'NumericFeature')
print(outliers_df)
print(summary_df)
```

## API Reference

### `analyze_categorical_feature(df, feature, target="Transported")`

- **df** (pd.DataFrame): The input DataFrame.
- **feature** (str): The categorical feature to analyze.
- **target** (str): The target variable for comparison. Default is `"Transported"`.

**Returns**:

- `pd.DataFrame`: Summary of the analysis.

### `analyze_numerical_feature(df, feature_col, target_col=None, figsize=(15, 6), bins=30)`

- **df** (pd.DataFrame): The input DataFrame.
- **feature_col** (str): The numerical feature to analyze.
- **target_col** (str, optional): The target variable for comparison.
- **figsize** (tuple, optional): Size of the output plot.
- **bins** (int, optional): Number of bins for the histogram.

**Returns**:

- `pd.DataFrame`: Outlier analysis summary.

## Contributing

Contributions are welcome! Please adhere to the following guidelines:

1. Fork the project repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add a new feature'`).
4. Push your changes to your branch (`git push origin feature-branch`).
5. Open a Pull Request with a detailed description of your changes.

### Running Tests

You can run the tests with `pytest`:

```bash
poetry run pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/surajwate/suraj_datalab/blob/master/LICENSE) file for more details.

## Acknowledgments

- Special thanks to [contributor names] for their input and code contributions.
- Inspired by other open-source data analysis tools.

## Contact

For questions or support, you can reach out.
