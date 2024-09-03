# Examples

This document provides practical examples of how to use the `suraj_datalab` package. Each example demonstrates a specific feature, complete with sample code and expected outputs.

## Example 1: Analyzing a Categorical Feature

### Scenario

You have a dataset with a categorical feature, and you want to analyze its distribution with respect to a target variable.

### Code

```python
import pandas as pd
from suraj_datalab import analyze

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A'],
    'Target': [1, 0, 1, 0, 1, 0, 0, 1]
}
df = pd.DataFrame(data)

# Analyze the categorical feature
distribution = analyze.categorical_feature(df, 'Category', 'Target')
print(distribution)
```

### Expected Output

```plaintext
  Total Count  Total Percentage  0 of Total (%)  1 of Total (%)  0 within Category (%)  1 within Category (%)
A            4              50.0            25.0            75.0                  25.0                  75.0
B            2              25.0            50.0            50.0                  50.0                  50.0
C            2              25.0            75.0            25.0                  75.0                  25.0
```

A plot showing the distribution of the `Category` feature by the `Target` variable will also be generated.

## Example 2: Analyzing a Numerical Feature

### Scenario

You want to analyze the distribution of a numerical feature, identify outliers, and visualize the data.

### Code

```python
import pandas as pd
from suraj_datalab import analyze

# Sample DataFrame
data = {
    'NumericalFeature': [10, 12, 10, 22, 23, 45, 47, 50],
    'Target': [1, 1, 0, 0, 1, 1, 0, 0]
}
df = pd.DataFrame(data)

# Analyze the numerical feature
outliers_df, summary_df = analyze.numerical_feature(df, 'NumericalFeature', 'Target')
print(outliers_df)
print(summary_df)
```

### Expected Output

```plaintext
   Outlier Percentage  Lower Outliers Percentage  Upper Outliers Percentage
0                 25.0                        0.0                       25.0

         count  mean  std   min   25%   50%   75%   max
Overall     8  27.375  18.518  10.0  12.5  22.5  46.5  50.0
Lower_Outliers 0  NaN   NaN    NaN   NaN   NaN   NaN   NaN
Upper_Outliers 2  48.5   1.5  47.0  47.75  48.5  49.25  50.0
```

Histograms and boxplots for the `NumericalFeature` will be generated.

## Example 3: Handling Missing Values

### Scenario

You have a dataset with missing values and want to generate a summary.

### Code

```python
import pandas as pd
from suraj_datalab import analyze

# Sample DataFrame
data = {
    'Feature1': [1, 2, None, 4, 5],
    'Feature2': [None, 2, 3, 4, None],
    'Feature3': [1, None, 3, None, 5]
}
df = pd.DataFrame(data)

# Get missing values summary
missing_summary = analyze.missing_values(df)
print(missing_summary)
```

### Expected Output

```plaintext
          Missing Count  Missing Percentage  Data Type
Feature1              1                20.0    float64
Feature2              2                40.0    float64
Feature3              2                40.0    float64
```

## Example 4: Replacing Rare Categories

### Scenario

You need to replace rare categories in your dataset with a specified value.

### Code

```python
import pandas as pd
from suraj_datalab.clean import RareCategoryReplacer

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'D', 'E', 'F', 'A'],
}
df = pd.DataFrame(data)

# Define the columns to replace rare categories in
columns_to_replace = ['Category']

# Create an instance of the RareCategoryReplacer
replacer = RareCategoryReplacer(columns=columns_to_replace, proportion_threshold=0.2, replacement_value="Others")

# Fit and transform the dataset
df_transformed = replacer.fit_transform(df)
print(df_transformed)
```

### Expected Output

```plaintext
  Category
0        A
1        B
2    Others
3        A
4        B
5        A
6    Others
7    Others
8    Others
9    Others
10       A
```

## Example 5: Creating K-Folds

### Scenario

You want to create K-Folds for cross-validation on a dataset.

### Code

```python
from suraj_datalab.fold_creator import create_kfolds

# Create K-Folds for a dataset
kfold_data = create_kfolds(file_path="your_dataset.csv", n_splits=5, shuffle=True, random_state=42)
print(kfold_data.head())
```

### Expected Output

A new CSV file with an additional `kfold` column indicating the fold assignment for each row in the dataset.

```plaintext
   Feature1  Feature2  kfold
0       ...       ...      0
1       ...       ...      1
2       ...       ...      4
3       ...       ...      3
4       ...       ...      2
```

## Example 6: Stratified K-Folds for Classification

### Scenario

You want to create stratified K-Folds for a classification problem to ensure balanced folds.

### Code

```python
from suraj_datalab.fold_creator import create_classification_kfolds

# Create Stratified K-Folds for a classification dataset
stratified_classification_data = create_classification_kfolds(
    file_path="your_dataset.csv", target_column="target", n_splits=5, random_state=42
)
print(stratified_classification_data.head())
```

### Expected Output

A new CSV file with an additional `kfold` column indicating the fold assignment, stratified by the target variable.

```plaintext
   Feature1  Feature2  target  kfold
0       ...       ...      0      1
1       ...       ...      1      3
2       ...       ...      0      4
3       ...       ...      1      0
4       ...       ...      1      2
```

## Example 7: Stratified K-Folds for Regression with Sturges' Binning

### Scenario

You want to create stratified K-Folds for a regression problem using Sturges' binning method.

### Code

```python
from suraj_datalab.fold_creator import create_regression_kfolds

# Create Stratified K-Folds for a regression dataset using 'sturges' binning method
stratified_regression_data = create_regression_kfolds(
    file_path="your_dataset.csv", target_column="target", n_splits=5, binning_method='sturges', random_state=42
)
print(stratified_regression_data.head())
```

### Expected Output

A new CSV file with an additional `kfold` column indicating the fold assignment, with the target variable stratified using Sturges' binning method.

```plaintext
   Feature1  Feature2  target  kfold
0       ...       ...    1.5      1
1       ...       ...    2.1      3
2       ...       ...    3.4      0
3       ...       ...    2.9      4
4       ...       ...    3.8      2
```
