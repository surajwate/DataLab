from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class RareCategoryReplacer(BaseEstimator, TransformerMixin):
    """
    Transformer class to replace rare categories in specified columns of a DataFrame.
    Parameters:
    -----------
    columns : list
        List of column names to replace rare categories in.
    proportion_threshold : float, optional (default=0.02)
        The threshold below which a category is considered rare.
    replacement_value : str, optional (default='Others')
        The value to replace rare categories with.
    Attributes:
    -----------
    rare_categories_ : dict
        A dictionary containing the rare categories for each specified column.
    Methods:
    --------
    fit(X, y=None)
        Fit the transformer to the data and calculate the rare categories for each specified column.
        Parameters:
        -----------
        X : pandas.DataFrame
            The input DataFrame.
        y : array-like, optional (default=None)
            The target variable. Not used in this transformer.
        Returns:
        --------
        self : RareCategoryReplacer
            The fitted transformer instance.
    transform(X)
        Transform the input DataFrame by replacing rare categories with the replacement value for each specified column.
        Parameters:
        -----------
        X : pandas.DataFrame
            The input DataFrame.
        Returns:
        --------
        X_transformed : pandas.DataFrame
            The transformed DataFrame with rare categories replaced.
    """
    def __init__(self, columns, proportion_threshold=0.02, replacement_value='Others'):
        self.columns = columns
        self.proportion_threshold = proportion_threshold
        self.replacement_value = replacement_value
        self.rare_categories_ = {}

    def fit(self, X, y=None):
        # Calculate the percentage of each category for each specified column
        for column in self.columns:
            category_percentages = X[column].value_counts(normalize=True)
            self.rare_categories_[column] = category_percentages[category_percentages < self.proportion_threshold].index

        return self

    def transform(self, X):
        X = X.copy()  # Create a copy of the DataFrame to avoid modifying the original data

        # Replace rare categories with the replacement value for each specified column
        for column in self.columns:
            rare_categories = self.rare_categories_.get(column, [])
            X[column] = np.where(X[column].isin(rare_categories), self.replacement_value, X[column])

        return X

# Example usage:
# columns_to_replace = ['cap-shape', 'cap-color', 'gill-color']
# replacer = RareCategoryReplacer(columns=columns_to_replace, proportion_threshold=0.02)
# df_train = replacer.fit_transform(df_train)  # Fit and transform on training data
# df_test = replacer.transform(df_test)        # Transform test data using the same categories
