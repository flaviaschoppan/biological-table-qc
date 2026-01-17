import pandas as pd

def check_missing_values(df: pd.DataFrame):
    """
    Returns a table with the number of missing values per column.
    """
    missing = df.isna().sum()
    return missing


def check_invalid_pvalues(df: pd.DataFrame):
    """
    Returns rows where p_value is outside the valid range [0, 1].
    """
    # Try to coerce to numeric, invalid parsing becomes NaN
    pvals = pd.to_numeric(df["p_value"], errors="coerce")

    invalid = df[(pvals < 0) | (pvals > 1)]
    return invalid

def check_negative_expression(df: pd.DataFrame):
    """
    Returns rows where mean_expression is negative.
    """
    expr = pd.to_numeric(df["mean_expression"], errors="coerce")
    return df[expr < 0]


def check_non_numeric_log2fc(df: pd.DataFrame):
    """
    Returns rows where log2FC is not numeric.
    """
    logfc = pd.to_numeric(df["log2FC"], errors="coerce")
    return df[logfc.isna()]


def check_extreme_expression(df: pd.DataFrame, threshold=1e7):
    """
    Returns rows where mean_expression is unrealistically large.
    """
    expr = pd.to_numeric(df["mean_expression"], errors="coerce")
    return df[expr > threshold]

