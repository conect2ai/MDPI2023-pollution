from sklearn.model_selection import train_test_split


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the data into training and test sets.

    Args:
        X (np.ndarray): Data.
        y (np.ndarray): Labels.
        test_size (float, optional): Size of the test set. Defaults to 0.2.
        random_state (int, optional): Random state. Defaults to 42.

    Returns:
        np.ndarray: Training data.
        np.ndarray: Test data.
        np.ndarray: Training labels.
        np.ndarray: Test labels.
    """

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test

def compute_co2(afr, maf, fuel_type):
    """
    Compute the CO2 emissions.

    Args:
        afr (np.ndarray): Array of AFR values.
        maf (np.ndarray): Array of MAF values.

    Returns:
        np.ndarray: Array of CO2 emissions.
    """

    if fuel_type == "gasoline":
        fuel_density = 737         # (g/L)
        emission_factor_CO2 = 2310 # (g/L)

    if fuel_type == "ethanol":
        fuel_density = 789         # (g/L)
        emission_factor_CO2 = 1510 # (g/L)

    fuel_volume = maf / (afr * fuel_density) # (g/s) / (1 * (g/L)) = (L/s)
    co2_emission = fuel_volume * emission_factor_CO2 # (L/s) * (g/L) = (g/s)

    return co2_emission