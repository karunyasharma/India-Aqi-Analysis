import pandas as pd


def load_data(filepath):
    """Load dataset from CSV."""
    return pd.read_csv(filepath)


def convert_date(df, column="Date"):
    """Convert the specified column to datetime."""
    df[column] = pd.to_datetime(df[column], errors="coerce")
    return df


def check_missing_values(df):
    """Return missing values count for each column."""
    return df.isnull().sum()


def interpolate_missing_values(df, columns):
    """Interpolate missing values in numeric columns."""
    df[columns] = df[columns].interpolate(method="linear", limit_direction="both")
    return df


def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates()


def remove_remaining_missing(df):
    """Drop rows that still contain missing values."""
    return df.dropna()


def save_clean_data(df, filepath):
    """Save cleaned dataset."""
    df.to_csv(filepath, index=False)
    print(f"Cleaned data saved to {filepath}")
