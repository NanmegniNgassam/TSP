"""
Gilles NGASSAM
26/01/2024
"""
# librairies importation
import numpy as np
import random as rd
from utils.Point import Point, generateRandomPoint

# General data
FLOATING_POINT = 0
NUMBER_OF_CITIES = 10
MIN_COORDINATE = 0
MAX_COORDINATE = 2000
MAX_DISTANCE=2000

# generate an array of cities
def generateCities(number_of_cities: int) -> list[Point]:
    """
    randomly generate an array of strictly differents cities

    Args:
        number of cities (int): the number of cities contained in the returned array

    Returns:
        list[Point]: a list of cities
    """
    cities: list[Point] = []

    while cities.__len__() < number_of_cities:
        city = generateRandomPoint(MIN_COORDINATE, MAX_COORDINATE, FLOATING_POINT)
        # Assure that two cities won't ever be identical
        if not cities.__contains__(city):
            cities.append(city)

    return cities