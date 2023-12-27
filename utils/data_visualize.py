import folium

import pandas as pd


def create_intervals(column: pd.Series, color_list: list) -> dict:
    """
    Create intervals for each color in color_list based on the column values.

    Args:
        column (pd.Series): Column of the dataframe.
        color_list (list): List of colors.

    Returns:
        dict: Dictionary of intervals.
    """

    n_intervals = len(color_list)
    min = column.min()
    max = column.max()
    increment = (max - min) / n_intervals

    intervals = {}

    for idx, color in enumerate(color_list):
        intervals[color] = min + (idx + 1) * increment

    return intervals

def column_to_colors(column: pd.Series, color_list: list = None, intervals: dict = None) -> list:
    """
    Convert the column values to colors.

    Args:
        column (pd.Series): Column of the dataframe.
        color_list (list, optional): List of colors. Defaults to None.
        intervals (dict, optional): Dictionary of intervals. Defaults to None.

    Returns:
        list: List of colors.
    """

    result = []

    if not intervals and not color_list:
        return result

    if not color_list and intervals:
        color_list = list(intervals.keys())

    if not intervals and color_list:
        intervals = create_intervals(column, color_list)

    for value in column:
        for color in color_list:
            if value <= intervals[color]:
                result.append(color)

                break

    return result

def routeplot(df: pd.DataFrame, column: str, color_list: list = None, intervals: dict = None):
    """
    Plot the route on a map.

    Args:
        df (pd.DataFrame): Dataframe.
        column (str): Column of the dataframe.
        color_list (list, optional): List of colors. Defaults to None.
        intervals (dict, optional): Dictionary of intervals. Defaults to None.

    Returns:
        folium.Map: Map with the route.
    """

    lat = df["Latitude"]
    lon = df["Longitude"]

    points    = list(zip(lat, lon))
    route_map = folium.Map(location=[-5.8204, -35.2085], zoom_start=14)

    folium.TileLayer('cartodbpositron').add_to(route_map)
  
    polilyne  = folium.PolyLine(points, color="red").add_to(route_map)

    points_column = polilyne.locations

    colors = column_to_colors(df[column], color_list, intervals)

    for i, point in enumerate(points_column):
        cor = colors[i]

        if i > 0:
            folium.PolyLine(locations=[points_column[i-1], point], weight=5, color=cor).add_to(route_map)

    start_trip = [points[0][0], points[0][1]]
    final_trip = [points[-1][0], points[-1][1]]

    icon_start_trip = folium.Marker(
        location=start_trip, 
        popup=folium.Popup(' Start '),
        icon=folium.Icon(color='green', prefix='fa', icon='fa-solid fa-flag-checkered')
    )

    icon_final_trip = folium.Marker(
        location=final_trip, 
        popup=folium.Popup(' Arrival '),
        icon=folium.Icon(color='red', prefix='fa', icon='fa-solid fa-flag-checkered')
    )

    icon_start_trip.add_to(route_map)
    icon_final_trip.add_to(route_map)

    return route_map