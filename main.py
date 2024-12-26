from models.City import generateCities, processDistanceMatrix

# launch the main function
cities = generateCities(8)

distances_matrix = processDistanceMatrix(cities, 2)

print(distances_matrix)