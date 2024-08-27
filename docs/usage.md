# Usage Guide for Suraj DataLab

This guide provides detailed instructions and examples on how to use the functions provided by the `suraj_datalab` package.

## `analyze_data` Function

The `analyze_data` function is designed to provide a quick statistical analysis of your dataset. Here’s how you can use it:

### Example

```python
import pandas as pd
from suraj_datalab.analysis import analyze_data

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Analyze the data
analyze_data(df)
```

This will output a summary of the dataset, including basic statistical measures like mean, median, and standard deviation for each column.

## `summary_statistics` Function

The `summary_statistics` function generates comprehensive summary statistics for your dataset. 

### Example

```python
import pandas as pd
from suraj_datalab.analysis import summary_statistics

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Generate summary statistics
summary = summary_statistics(df)
print(summary)
```

This will return a pandas DataFrame with summary statistics such as count, mean, standard deviation, min, max, and percentiles.

## Cross-references

For a general overview and more information about the project, please visit the [Project Overview](index.md).

## Additional Resources

For more details about my work and other projects, visit my [personal website](https://surajwate.com).

---

If you have any questions or run into issues, please check the [GitHub repository](https://github.com/surajwate/DataLab) for additional help or to open an issue.
