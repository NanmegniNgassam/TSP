from models.City import generateCities, processDistanceMatrix
from vue.visualization import path_visualization
from models.Plan import process_tour_total_distance, generate_derivated_plan

# launch the main function
cities = generateCities(8)
distances_matrix = processDistanceMatrix(cities, 0)

plan = cities
derivated_plan = generate_derivated_plan(plan)

print("The total distance of the tour is: ", process_tour_total_distance(plan))
path_visualization(plan)

print("The total distance of the derivated tour is: ", process_tour_total_distance(derivated_plan))
path_visualization(derivated_plan)