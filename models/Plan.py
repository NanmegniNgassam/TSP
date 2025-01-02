"""
Gilles NGASSAM
02/01/2024
"""

# librairies importation
import random as rd
from copy import deepcopy
from utils.Point import Point

# Calculate the total distance of the tour
def process_tour_total_distance(plan: list[Point]) -> float:
    """
    Calculate the total distance of the tour

    Args:
        plan (list[Point]): a group of cities in the order to visit

    Returns:
        float: the total distance of the tour
    """
    total_distance: float = 0

    for i in range(plan.__len__()):
        total_distance += plan[i].calculateDistanceTo(plan[(i+1)%plan.__len__()])

    return total_distance

# Generate a new plan from the previous one by swapping two cities
def generate_derivated_plan(plan: list[Point]) -> list[Point]:
    """
    Generate a new plan from the previous one by swapping two cities

    Args:
        plan (list[Point]): the previous plan (a group of cities in the order to visit)

    Returns:
        list[Point]: the new plan derived from the given one
    """
    # Copy the previous plan
    new_plan: list[Point] = deepcopy(plan)

    # Swap the two cities
    exchange_array: list[int] = rd.sample(range(0, plan.__len__()), 2)
    new_plan[exchange_array[0]], new_plan[exchange_array[1]] = new_plan[exchange_array[1]], new_plan[exchange_array[0]]

    return new_plan