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


# process the distance's matrix from the cities
def processDistanceMatrix(cities: list[Point], accuracy: int) -> list[list[float]]:
    """
    generate the distance matrix, knowing a group of cities

    Args:
        cities (list[Point]): a group of cities
        accuracy (int): the accuracy of distance from the floating' point of view

    Returns:
        list[list[float]]: a matrix of interralated distances between each city and the others 
    """
    # initialize the matrix
    distances_matrix: list[list[float|int]] = np.zeros((cities.__len__(), cities.__len__()))

    # Go through the cities and sequentially pick one of them
    for i,city in enumerate(cities):
        # With a selected city, process the distance between it and the others cities
        for j, neighbourCity in enumerate(cities):
            distances_matrix[i][j] = round(city.calculateDistanceTo(neighbourCity), accuracy)
            distances_matrix[j][i] = distances_matrix[i][j]

    return distances_matrix