import pytest
import pandas as pd
from suraj_datalab.analysis import analyze_categorical_feature, analyze_numerical_feature

# Sample DataFrame for testing
def create_test_dataframe():
    data = {
        'Feature': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
        'Transported': [True, False, True, True, False, True, False, True, False, True],
        'NumericFeature': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return pd.DataFrame(data)

def test_analyze_categorical_feature():
    df = create_test_dataframe()
    result = analyze_categorical_feature(df, 'Feature')
    assert isinstance(result, pd.DataFrame)
    assert 'Count' in result.columns
    assert 'Percentage' in result.columns
    assert 'Transported' in result.columns
    assert 'Not Transported' in result.columns

def test_analyze_numerical_feature():
    # Create a test DataFrame
    df = pd.DataFrame({
        'NumericFeature': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    })
    
    # Run the function
    outliers_df, summary_df = analyze_numerical_feature(df, 'NumericFeature')

    # Check that the returned summary_df contains expected columns
    assert 'NumericFeature_Overall' in summary_df.index
    assert 'NumericFeature_Lower_Outliers' in summary_df.index
    assert 'NumericFeature_Upper_Outliers' in summary_df.index

    # Check the outliers_df contains the expected columns
    assert 'Outlier Percentage' in outliers_df.columns
    assert 'Lower Outliers Percentage' in outliers_df.columns
    assert 'Upper Outliers Percentage' in outliers_df.columns

