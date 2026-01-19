#16. You have a dataset with a 'date' column in the format 'YYYY-MM-DD HH:MM:SS'.

# Write a Python function to convert this column to a datetime object and create new 
# columns for the year, month, day, hour, minute, and second.
# Example usage 

# date_data = pd.DataFrame({'date': ['2022-01-01 12:30:45', '2022-02-03 08:15: 20']})

import pandas as pd

def extract_datetime_features(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Converts a string column to datetime and extracts year, month, 
    day, hour, minute, and second into new columns.
    """
    # 1. Convert the column to datetime objects
    df[column_name] = pd.to_datetime(df[column_name])
    
    # 2. Extract components using the .dt accessor
    df['year'] = df[column_name].dt.year
    df['month'] = df[column_name].dt.month
    df['day'] = df[column_name].dt.day
    df['hour'] = df[column_name].dt.hour
    df['minute'] = df[column_name].dt.minute
    df['second'] = df[column_name].dt.second
    
    return df

# --- Example Usage ---
date_data = pd.DataFrame({
    'date': ['2022-01-01 12:30:45', '2022-02-03 08:15:20']
})

processed_df = extract_datetime_features(date_data, 'date')
print(processed_df)