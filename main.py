from models.City import generateCities, processDistanceMatrix
from vue.visualization import path_visualization
from models.Plan import process_tour_total_distance

# launch the main function
cities = generateCities(8)
distances_matrix = processDistanceMatrix(cities, 0)

print("The total distance of the tour is: ", process_tour_total_distance(cities))
path_visualization(cities)