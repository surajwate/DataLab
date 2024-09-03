# Usage

This document provides a guide on how to use the `suraj_datalab` package for data analysis.

## Installation

Ensure that you have all the necessary dependencies installed by running:

```bash
pip install -r requirements.txt
```

## Importing the Package

To use the `suraj_datalab` package in your Python script, you need to import it as follows:

```python
from suraj_datalab import analyze, clean, fold_creator
```

## Analyzing Categorical Features

The `categorical_feature` function allows you to analyze the distribution of a categorical feature with respect to a target variable. This function is useful for understanding how different categories are distributed and how they relate to the target variable.

### Example Usage

```python
import pandas as pd
from suraj_datalab import analyze

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Analyze a categorical feature
distribution = analyze.categorical_feature(df, 'feature_name', 'target_name')
print(distribution)
```

### Output

The output is a DataFrame showing:

- Total Count
- Total Percentage
- Percentages for each target class relative to the total
- Percentages of each target class within the feature category

A plot is also generated, showing the distribution of the feature by the target variable.

## Analyzing Numerical Features

The `numerical_feature` function allows you to analyze the distribution of a numerical feature, with optional grouping by a target variable. This function provides detailed statistics, including outlier detection.

### Example Usage

```python
import pandas as pd
from suraj_datalab import analyze

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Analyze a numerical feature
outliers_df, summary_df = analyze.numerical_feature(df, 'numerical_feature_name', 'target_name')
print(outliers_df)
print(summary_df)
```

### Output

The function returns:

- `outliers_df`: A DataFrame containing the percentage of outliers.
- `summary_df`: A DataFrame with overall statistics, as well as statistics for lower and upper outliers.

A histogram and boxplot are also generated to visualize the distribution.

## Missing Values Summary

The `missing_values` function generates a summary of missing values in the DataFrame.

### Example Usage

```python
import pandas as pd
from suraj_datalab import analyze

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Get missing values summary
missing_summary = analyze.missing_values(df)
print(missing_summary)
```

### Output

The function returns a DataFrame with the following information:

- Count of missing values
- Percentage of missing values
- Data type of each column that has missing values

## Handling Rare Categories in Categorical Features

The `RareCategoryReplacer` class in `clean.py` is used to replace rare categories in specified columns of a DataFrame with a replacement value.

### Example Usage

```python
import pandas as pd
from suraj_datalab.clean import RareCategoryReplacer

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Define the columns to replace rare categories in
columns_to_replace = ['feature_1', 'feature_2']

# Create an instance of the RareCategoryReplacer
replacer = RareCategoryReplacer(columns=columns_to_replace, proportion_threshold=0.02, replacement_value="Others")

# Fit and transform the dataset
df_transformed = replacer.fit_transform(df)
print(df_transformed)
```

### Output

The output is a transformed DataFrame where rare categories in the specified columns are replaced with the value "Others".

## Creating K-Folds for Cross-Validation

The `fold_creator.py` script provides functions to create K-Folds for cross-validation, including standard K-Folds, stratified K-Folds for classification, and stratified K-Folds for regression tasks.

### Example Usage for K-Folds

```python
from suraj_datalab.fold_creator import create_kfolds

# Create K-Folds for a dataset
kfold_data = create_kfolds(file_path="your_dataset.csv", n_splits=5, shuffle=True, random_state=42)
print(kfold_data)
```

### Example Usage for Stratified K-Folds (Classification)

```python
from suraj_datalab.fold_creator import create_classification_kfolds

# Create Stratified K-Folds for a classification dataset
stratified_classification_data = create_classification_kfolds(
    file_path="your_dataset.csv", target_column="target", n_splits=5, random_state=42
)
print(stratified_classification_data)
```

### Example Usage for Stratified K-Folds (Regression)

```python
from suraj_datalab.fold_creator import create_regression_kfolds

# Create Stratified K-Folds for a regression dataset using 'sturges' binning method
stratified_regression_data = create_regression_kfolds(
    file_path="your_dataset.csv", target_column="target", n_splits=5, binning_method='sturges', random_state=42
)
print(stratified_regression_data)
```

### Output

Each of these functions will return a DataFrame with an additional 'kfold' column, indicating the fold assignment for each row in the dataset. The `create_regression_kfolds` function offers several methods for binning the target variable before applying stratified K-Folds, such as 'sturges', 'quantile', 'kmeans', and custom binning.

## Cross-references

For a general overview and more information about the project, please visit the [Project Overview](index.md).

## Additional Resources

For more details about my work and other projects, visit my [personal website](https://surajwate.com).

---

If you have any questions or run into issues, please check the [GitHub repository](https://github.com/surajwate/DataLab) for additional help or to open an issue.
