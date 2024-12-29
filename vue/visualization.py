"""
Gilles NGASSAM
29/12/2024
"""

# librairies importation
from utils.Point import Point
from utils.parameters import MIN_COORDINATE, MAX_COORDINATE
import matplotlib.pyplot as plt


# Visualize the planned tour of the salesman
def path_visualization(cities: list[Point]) -> None:
    """
    Generate and show a 2-dimension map and place every cities and path between them

    Args:
        cities (list[Point]): a group of cities to display on the map
    """
    x_coords: list[float] = []
    y_coords: list[float] = []

    for city in cities:
        x_coords.append(city.x)
        y_coords.append(city.y)

    # Add the first point to make up a cycle
    x_coords.append(cities[0].x)
    y_coords.append(cities[0].y)

    plt.plot(x_coords, y_coords, "-sg")
    plt.ylim(MIN_COORDINATE, MAX_COORDINATE)
    plt.xlim(MIN_COORDINATE, MAX_COORDINATE)
    plt.ylabel("y-axis")
    plt.xlabel("x-axis")
    plt.title("Location of the tour cities")

    plt.show()
    return