# API Reference

This document provides a detailed reference for all the classes and functions available in the `suraj_datalab` package.

## Modules

- [analyze](#analyze-module)
- [clean](#clean-module)
- [fold_creator](#fold-creator-module)

## Analyze Module

### `categorical_feature(df, feature, target)`

Analyze the distribution of a categorical feature with respect to a target variable.

**Parameters:**

- `df (pandas.DataFrame)`: The input DataFrame.
- `feature (str)`: The name of the categorical feature to analyze.
- `target (str)`: The name of the target variable.

**Returns:**

- `pandas.DataFrame`: A DataFrame containing the distribution of the feature with respect to the target.

### `numerical_feature(df, feature, target=None, figsize=(15, 6), bins="sturges")`

Analyze the distribution of a numerical feature, with optional grouping by a target variable.

**Parameters:**

- `df (pandas.DataFrame)`: The input DataFrame.
- `feature (str)`: The name of the numerical feature to analyze.
- `target (str, optional)`: The name of the target column for grouping the analysis. Default is `None`.
- `figsize (tuple, optional)`: The size of the figure. Default is `(15, 6)`.
- `bins (int or str, optional)`: The number of bins or the method to calculate them. Default is `"sturges"`.

**Returns:**

- `pandas.DataFrame`: A DataFrame containing outlier percentages and summary statistics.

### `missing_values(dataframe)`

Generate a summary of missing values in the DataFrame.

**Parameters:**

- `dataframe (pandas.DataFrame)`: The input DataFrame.

**Returns:**

- `pandas.DataFrame`: A DataFrame containing missing values count, percentage, and data types for columns with missing values.

## Clean Module

### `RareCategoryReplacer(columns, proportion_threshold=0.02, replacement_value="Others")`

Class for replacing rare categories in specified columns of a DataFrame.

**Parameters:**

- `columns (list)`: List of column names to apply the rare category replacement.
- `proportion_threshold (float, optional)`: Threshold below which a category is considered rare. Default is `0.02`.
- `replacement_value (str, optional)`: Value to replace rare categories with. Default is `"Others"`.

**Attributes:**

- `rare_categories_ (dict)`: Dictionary containing the rare categories for each specified column.
- `important_categories_ (dict)`: Dictionary containing the important categories for each specified column.

**Methods:**

- `fit(X, y=None)`: Fit the transformer by calculating rare categories.
- `transform(X)`: Transform the data by replacing rare categories.
- `fit_transform(X, y=None)`: Fit and transform the data in a single step.

## Fold Creator Module

### `create_kfolds(file_path, n_splits=5, shuffle=True, random_state=42, save_path=None)`

Create K-Fold indices for a dataset loaded from a CSV file.

**Parameters:**

- `file_path (str)`: Path to the input CSV file.
- `n_splits (int, optional)`: Number of folds. Default is `5`.
- `shuffle (bool, optional)`: Whether to shuffle the data. Default is `True`.
- `random_state (int, optional)`: Seed for the random number generator. Default is `42`.
- `save_path (str, optional)`: Path to save the CSV file. If `None`, the file is not saved.

**Returns:**

- `pandas.DataFrame`: DataFrame with an additional `kfold` column.

### `create_classification_kfolds(file_path, target_column, n_splits=5, random_state=42, save_path=None)`

Create stratified K-Fold indices for classification tasks from a CSV file.

**Parameters:**

- `file_path (str)`: Path to the input CSV file.
- `target_column (str)`: The name of the target column.
- `n_splits (int, optional)`: Number of folds. Default is `5`.
- `random_state (int, optional)`: Seed for the random number generator. Default is `42`.
- `save_path (str, optional)`: Path to save the CSV file. If `None`, the file is not saved.

**Returns:**

- `pandas.DataFrame`: DataFrame with an additional `kfold` column.

### `create_regression_kfolds(file_path, target_column, n_splits=5, binning_method="sturges", custom_bins=None, random_state=42, save_path=None)`

Create stratified K-Fold indices for regression tasks using various binning methods from a CSV file.

**Parameters:**

- `file_path (str)`: Path to the input CSV file.
- `target_column (str)`: The name of the target column.
- `n_splits (int, optional)`: Number of folds. Default is `5`.
- `binning_method (str, optional)`: Method for binning the target variable. Options: `'sturges'`, `'quantile'`, `'kmeans'`, `'custom'`. Default is `'sturges'`.
- `custom_bins (list, optional)`: List of bin edges for custom binning. Required if `binning_method` is `'custom'`.
- `random_state (int, optional)`: Seed for the random number generator. Default is `42`.
- `save_path (str, optional)`: Path to save the CSV file. If `None`, the file is not saved.

**Returns:**

- `pandas.DataFrame`: DataFrame with an additional `kfold` column.

## Learn More

For detailed usage instructions, please visit the [Usage Guide](usage.md).

For more information about my work, other projects, or to get in touch, visit my [personal website](https://surajwate.com)

---

If you have any feedback or suggestions, feel free to open an issue on [GitHub](https://github.com/surajwate/DataLab).
