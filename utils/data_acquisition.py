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

def get_CO2(df: pd.DataFrame, fuel: str) -> pd.DataFrame:
    if fuel == "gasoline":
        fuel_density = 737         # (g/L)
        emission_factor_CO2 = 2310 # (g/L)

    if fuel == "ethanol":
        fuel_density = 789         # (g/L)
        emission_factor_CO2 = 1510 # (g/L)
    
    afr = df["AirFuelRatio(Commanded)(:1)"]
    maf = df["MassAirFlowRate(g/s)"]

    fuel_volume = maf / (afr * fuel_density) # (g/s) / (g/L) = (L/s


    co2_emission = fuel_volume * emission_factor_CO2 # (L/s) * (g/L) = (g/s)
    co2_emission = co2_emission * 1000 # (g/s) * 1000 = (mg/s)

    return co2_emission