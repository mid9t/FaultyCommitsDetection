from __future__ import annotations

from typing import List, Dict

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

import pandas as pd
import numpy as np
import torch


def compute_data_preprocessor(
        dataframe: pd.DataFrame,
        numerical_features: List[str],
        categorical_features: List[str],
) -> ColumnTransformer:
    """Given an input DataFrame, compute a ColumnTransformer that does the following:
    (Numerical features) standardize to 0 mean, 1.0 std
        Missing data imputation: use average value
    (Categorical features) encode as one-hot encoding.
        Missing data imputation: fill as "NotAvailable".
        If an unknown value is encountered, you should map this value to the "all 0's" encoding, eg set
            OneHotEncoder(...,handle_unknown="ignore", ...)
            Example: if during training, we see categorical values ["a", "b"], but during validation a row has value
                "c", then "c" should be mapped to be one-hot vector [0, 0].

    Any features not listed in `numerical_features, categorical_features` should be ignored (dropped).

    Args:
        dataframe: Dataframe from, say: data/split/faulty_commit_dev_train.csv
        numerical_features: List of dataframe column names to use as numerical features.
        categorical_features: List of dataframe column names to use as categorical features.

    Returns:
        preprocessor: a `ColumnTransformer` instance that can be used to preprocess training/val/test dataframes,
            eg via `preprocessor.transform(df_train)`.

    """
    # BEGIN YOUR CODE
    # END YOUR CODE
    return None


class FaultCSVDataset(torch.utils.data.Dataset):
    """Dataset for the faulty commit dataset.
    """
    def __init__(self, dataframe: pd.DataFrame, preprocessor: ColumnTransformer):
        """

        Args:
            dataframe: DataFrame from, say: data/split/faulty_commit_dev_train.csv
            preprocessor: see: compute_data_preprocessor()
        """
        self.dataframe = dataframe
        self.preprocessor = preprocessor

        # Hint: here, apply the preprocessor to all rows of the input dataframe to precompute  the preprocessed
        #   features, storing as an instance variable. Then, __getitem__() can be a simple lookup into this precomputed
        #   value.
        # Hint: to transform the 'faultbasis' column from its odd/even integer values to a 0/1 binary class label,
        #   note that `dataframe['some_int_column'] % 2` produces a new pd.Series with the modulo operator applied to
        #   each value.
        # BEGIN YOUR CODE
        # END YOUR CODE


    def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
        """Retrieves a single preprocessed row from the dataset.

        Args:
            idx: Row index to output from the dataset.

        Returns:
            row_dict: a Dict with the following keys:
                features: torch.Tensor. shape=[dim_feats]. dtype=torch.float32. Features with preprocessing applied
                    (eg standardization, one-hot encoding, etc).
                    The ordering of the columns of this tensor should look like:
                        [<numerical_features>, <categorical_features>]
                label: torch.Tensor. shape=[1]. dtype=torch.float32. Should be one of two values:
                    1: faulty commit ("positive class")
                    0: not-faulty commit ("negative class")
        """
        # BEGIN YOUR CODE
        # END YOUR CODE
        return {
            "features": torch.zeros([32], dtype=torch.float32),
            "label": torch.tensor([0.0], dtype=torch.float32),
        }

    def __len__(self) -> int:
        """Return the number of rows of this dataset.

        Returns:
            dataset_len:

        """
        # BEGIN YOUR CODE
        # END YOUR CODE
        return 0
