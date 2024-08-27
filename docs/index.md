# Welcome to the Suraj DataLab Documentation

Welcome to the documentation for the `suraj_datalab` Python package. This package provides simple yet effective data analysis tools to help you get insights from your data quickly. The goal of this package is to offer straightforward functions that cater to everyday data analysis needs.

## Installation

You can install the package via pip:

```bash
pip install suraj_datalab
```

## Project Overview

The `suraj_datalab` package currently includes two primary functions designed to streamline your data analysis workflow:

- **`analyze_data`:** Perform a quick statistical analysis on your dataset.
- **`summary_statistics`:** Generate summary statistics for a given dataset.

These functions are particularly useful for data scientists, analysts, and anyone working with data who needs quick insights without diving deep into complex analysis frameworks.

### Example Usage

Here's a quick example of how to use the main functions:

```python
from suraj_datalab.analysis import analyze_data, summary_statistics

# Assuming you have a pandas DataFrame `df`
analyze_data(df)
summary = summary_statistics(df)
print(summary)
```

## Learn More

For detailed usage instructions, please visit the [Usage Guide](usage.md).

For more information about my work, other projects, or to get in touch, visit my [personal website](https://surajwate.com)

---

If you have any feedback or suggestions, feel free to open an issue on [GitHub](https://github.com/surajwate/DataLab).
