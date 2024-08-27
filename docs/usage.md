# Usage Guide for Suraj DataLab

This guide will show you how to use the functions available in the **Suraj DataLab** package for analyzing categorical and numerical features.

## Analyzing Categorical Features

You can analyze categorical features in your dataset using the `analyze_categorical_feature` function. This function helps you understand the distribution of a categorical feature with respect to a target variable.

### Example Usage

```python
import pandas as pd
from suraj_datalab.analysis import analyze_categorical_feature

# Example dataframe
data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'C', 'A'],
    'Transported': [True, False, True, True, False, False, True]
}
df = pd.DataFrame(data)

# Analyze the 'Category' feature
summary_df = analyze_categorical_feature(df, feature='Category', target='Transported')

# View the summary
print(summary_df)
