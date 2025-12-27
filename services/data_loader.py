import pandas as pd
import os

# Cache the dataframe so Excel is loaded only once
_DATAFRAME = None


def load_data():
    global _DATAFRAME

    if _DATAFRAME is not None:
        return _DATAFRAME

    # Build path to Excel file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "superstore.xlsx")

    # Load Excel
    df = pd.read_excel(data_path)

    # Ensure date column is datetime
    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"])

    _DATAFRAME = df
    return df
