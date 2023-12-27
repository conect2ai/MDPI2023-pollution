"""
Utility functions for data acquisition
"""

import os

import pandas as pd


def get_list_paths(path: str) -> list:
    """
    Get the list of paths from a directory.
    
    Args:
        path (str): Path to the directory.
    
    Returns:
        list: List of paths.
    """

    return [path + file for file in os.listdir(path) if ".csv" in file]

def get_week_day(path: str) -> str:
  start_index = path.rfind('_') + 1
  end_index   = path.rfind('.csv')

  week_day = path[start_index:end_index].upper()

  return week_day

def get_data_info(path: str) -> pd.DataFrame:
  data_info = pd.DataFrame()

  for path in get_list_paths(path):
    data = pd.read_csv(path)

    new_row = pd.DataFrame({
      "PATH":     path,
      "WEEK_DAY": get_week_day(path),
      "ROWS": data.shape[0]
    }, index=[0])

    data_info = pd.concat([data_info, new_row], ignore_index=True)

  return data_info

def select_by_similarity(l1: list, l2: list) -> list:
  result = []

  for v1 in l1:
    for v2 in l2:
      if len(result) == 0 or abs(v1 - v2) < diff:
        result = [v1, v2]
        diff   = abs(v1 - v2)

  print(f"Differece: {diff}")
  
  return result

def read_all_data(list_paths: list) -> pd.DataFrame:
    """
    Read all the data with .csv extension from the list of paths and return a list of dataframes.
    
    Args:
        list_paths (list): List of paths to the data.
    
    Returns:
        (list): List of dataframes (one dataframe per file
    """

    return [pd.read_csv(path) for path in list_paths if ".csv" in path]

def concatenate_dataframes(list_df: list) -> pd.DataFrame:
    """
    Concatenate a list of dataframes.
    
    Args:
        list_df (list): List of dataframes.
    
    Returns:
        pd.DataFrame: Dataframe with all the dataframes concatenated.
    """

    return pd.concat(list_df, ignore_index=True)

def remove_space_in_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove the space in the columns of the dataframe.
    
    Args:
        df (pd.DataFrame): Dataframe to remove the spaces.
    
    Returns:
        pd.DataFrame: Dataframe without spaces in the columns.
    """

    df.columns = df.columns.str.replace(" ", "")

    return df

def filter_columns(df: pd.DataFrame, list_columns: list) -> pd.DataFrame:
    """
    Filter the columns of the dataframe.
    
    Args:
        df (pd.DataFrame): Dataframe to filter the columns.
        list_columns (list): List of columns to keep.
    
    Returns:
        pd.DataFrame: Dataframe with the filtered columns.
    """

    return df[list_columns]

def compute_acceleration(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the acceleration of the dataframe. The time step is 1 second,
    so the acceleration is the difference between the speed at time t and
    the speed at time t-1.
    
    Args:
        df (pd.DataFrame): Dataframe to compute the acceleration.
    
    Returns:
        pd.DataFrame: Dataframe with the acceleration.
    """

    return df["Speed(OBD)(km/h)"].diff()