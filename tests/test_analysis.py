import pytest
import pandas as pd
import numpy as np
from suraj_datalab.analyze import categorical_feature, numerical_feature, missing_values
import matplotlib.pyplot as plt
import os

def test_categorical_feature():
    # Create a test DataFrame
    data = {
        'Feature': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
        'Target': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
    }
    df = pd.DataFrame(data)

    # Call the categorical_feature function
    category_distribution = categorical_feature(df, 'Feature', 'Target')

    # Check the output DataFrame
    expected_columns = [
        'Total Count', 'Total Percentage', 
        'X of Total (%)', 'Y of Total (%)', 'Z of Total (%)',
        'X within Feature (%)', 'Y within Feature (%)', 'Z within Feature (%)'
    ]
    assert category_distribution.columns.tolist() == expected_columns
    assert category_distribution.index.tolist() == ['A', 'B', 'C']
    assert category_distribution.loc['A', 'Total Count'] == 3
    assert category_distribution.loc['B', 'Total Percentage'] == pytest.approx(33.33, rel=1e-2)

def test_categorical_feature_plot(tmpdir):
    # Create a test DataFrame
    data = {
        'Feature': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
        'Target': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
    }
    df = pd.DataFrame(data)

    # Set the plot directory to a temporary directory
    plot_dir = tmpdir.mkdir("plots")
    plot_path = os.path.join(plot_dir, "plot.png")

    # Call the categorical_feature function
    category_distribution = categorical_feature(df, 'Feature', 'Target')

    # Save the plot to the temporary directory
    plt.savefig(plot_path)

    # Check the plot
    assert plt.gcf().get_size_inches().tolist() == [12, 6]
    assert plt.gca().get_title() == 'Distribution of Feature by Target'
    assert plt.gca().get_xlabel() == 'Feature'
    assert plt.gca().get_ylabel() == 'count'
    assert os.path.exists(plot_path)

def test_numerical_feature(tmpdir):
    # Create a test DataFrame
    data = {
        'Feature': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Target': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
    }
    df = pd.DataFrame(data)

    # Set the plot directory to a temporary directory
    plot_dir = tmpdir.mkdir("plots")
    plot_path = os.path.join(plot_dir, "plot.png")

    # Call the numerical_feature function
    outliers_df, summary_df = numerical_feature(df, feature='Feature', target='Target')

    # Save the plot to the temporary directory
    plt.savefig(plot_path)

    # Check the output of outliers_df
    assert outliers_df['Outlier Percentage'][0] == 0.0
    assert outliers_df['Lower Outliers Percentage'][0] == 0.0
    assert outliers_df['Upper Outliers Percentage'][0] == 0.0

    # Check the output of summary_df
    assert summary_df.loc['Feature_Overall', 'count'] == 10.0
    assert summary_df.loc['Feature_Overall', 'mean'] == 5.5
    assert summary_df.loc['Feature_Overall', 'std'] == pytest.approx(3.03, rel=1e-2)
    assert summary_df.loc['Feature_Overall', 'min'] == 1.0
    assert summary_df.loc['Feature_Overall', '25%'] == 3.25
    assert summary_df.loc['Feature_Overall', '50%'] == 5.5
    assert summary_df.loc['Feature_Overall', '75%'] == 7.75
    assert summary_df.loc['Feature_Overall', 'max'] == 10.0

    # Check the plot
    assert len(plt.gcf().axes) == 2
    assert plt.gcf().axes[0].get_title() == 'Distribution of Feature with KDE'
    assert plt.gcf().axes[1].get_title() == 'Box Plot of Feature by Target Status'
    assert plt.gcf().axes[0].get_ylabel() == 'Frequency'
    assert plt.gcf().axes[1].get_ylabel() == ''
    assert plt.gcf().axes[0].get_xlabel() == 'Feature'
    assert plt.gcf().axes[1].get_xlabel() == 'Feature'
    assert os.path.exists(plot_path)

def test_missing_values():
    # Create a test DataFrame
    data = {
        'Feature1': [1, 2, np.nan, 4, 5],
        'Feature2': [np.nan, 2, np.nan, 4, 5],
        'Feature3': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)

    # Call the missing_values function
    missing_summary = missing_values(df)

    # Check the output DataFrame
    assert 'Missing Count' in missing_summary.columns
    assert 'Missing Percentage' in missing_summary.columns
    assert 'Data Type' in missing_summary.columns

    assert missing_summary.loc['Feature1', 'Missing Count'] == 1
    assert missing_summary.loc['Feature1', 'Missing Percentage'] == 20.0
    assert missing_summary.loc['Feature1', 'Data Type'] == 'float64'

    assert missing_summary.loc['Feature2', 'Missing Count'] == 2
    assert missing_summary.loc['Feature2', 'Missing Percentage'] == 40.0
    assert missing_summary.loc['Feature2', 'Data Type'] == 'float64'

    # Feature3 should not appear in the summary because it has no missing values
    assert 'Feature3' not in missing_summary.index
