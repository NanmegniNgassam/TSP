"""
Gilles NGASSAM
02/01/2024
"""

# librairies importation
from utils.Point import Point

# Calculate the total distance of the tour
def process_tour_total_distance(cities: list[Point]) -> float:
    """
    Calculate the total distance of the tour

    Args:
        cities (list[Point]): a group of cities in the order to visit

    Returns:
        float: the total distance of the tour
    """
    total_distance: float = 0

    for i in range(cities.__len__()):
        total_distance += cities[i].calculateDistanceTo(cities[(i+1)%cities.__len__()])

    return total_distance