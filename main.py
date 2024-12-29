from models.City import generateCities, processDistanceMatrix
from vue.visualization import path_visualization

# launch the main function
cities = generateCities(8)
distances_matrix = processDistanceMatrix(cities, 0)
path_visualization(cities)

print(distances_matrix)