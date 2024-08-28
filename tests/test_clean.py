import pytest
import pandas as pd
from suraj_datalab.clean import RareCategoryReplacer

def test_rare_category_replacer_fit():
    # Create a test DataFrame
    data = {
        'Column1': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Column2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Column3': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    }
    df = pd.DataFrame(data)

    # Create an instance of RareCategoryReplacer
    replacer = RareCategoryReplacer(columns=['Column1', 'Column2', 'Column3'], proportion_threshold=0.2)

    # Fit the transformer
    replacer.fit(df)

    # Check that the rare_categories_ attribute is correctly populated
    assert replacer.rare_categories_ == {'Column1': [], 'Column2': [], 'Column3': []}

def test_rare_category_replacer_transform():
    # Create a test DataFrame
    data = {
        'Column1': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Column2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Column3': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    }
    df = pd.DataFrame(data)

    # Create an instance of RareCategoryReplacer
    replacer = RareCategoryReplacer(columns=['Column1', 'Column2', 'Column3'], proportion_threshold=0.2)

    # Fit and transform the DataFrame
    transformed_df = replacer.fit_transform(df)

    # Check that the rare categories are replaced with the replacement value
    assert transformed_df['Column1'].value_counts()['Others'] == 0
    assert transformed_df['Column2'].value_counts()['Others'] == 0
    assert transformed_df['Column3'].value_counts()['Others'] == 0