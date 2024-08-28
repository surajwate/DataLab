import pytest
import pandas as pd
import numpy as np  # Import numpy
from suraj_datalab.clean import RareCategoryReplacer

def test_rare_category_replacer_fit():
    # Create a test DataFrame with some rare categories
    data = {
        'Column1': ['A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F'],
        'Column2': ['A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F'],
        'Column3': ['A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F']
    }
    df = pd.DataFrame(data)

    # Create an instance of RareCategoryReplacer
    replacer = RareCategoryReplacer(columns=['Column1', 'Column2', 'Column3'], proportion_threshold=0.2)

    # Fit the transformer
    replacer.fit(df)

    # Check that the rare_categories_ attribute is correctly populated
    expected_rare_categories = {
        'Column1': ['B', 'C', 'D', 'E', 'F'],
        'Column2': ['B', 'C', 'D', 'E', 'F'],
        'Column3': ['B', 'C', 'D', 'E', 'F']
    }
    for column in expected_rare_categories:
        assert np.array_equal(replacer.rare_categories_[column], expected_rare_categories[column])

def test_rare_category_replacer_transform():
    # Create a test DataFrame with some rare categories
    data = {
        'Column1': ['A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F'],
        'Column2': ['A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F'],
        'Column3': ['A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F']
    }
    df = pd.DataFrame(data)

    # Create an instance of RareCategoryReplacer
    replacer = RareCategoryReplacer(columns=['Column1', 'Column2', 'Column3'], proportion_threshold=0.2)

    # Fit and transform the DataFrame
    transformed_df = replacer.fit_transform(df)

    # Check that the rare categories are replaced with the replacement value
    assert (transformed_df['Column1'] == 'Others').sum() == 5
    assert (transformed_df['Column2'] == 'Others').sum() == 5
    assert (transformed_df['Column3'] == 'Others').sum() == 5

    # Check that the non-rare categories are not replaced
    assert (transformed_df['Column1'] == 'A').sum() == 5
    assert (transformed_df['Column2'] == 'A').sum() == 5
    assert (transformed_df['Column3'] == 'A').sum() == 5