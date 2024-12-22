## Traveling Salesman Problem (TSP)

The Traveling Salesman Problem (TSP) is a classic optimization problem in combinatorial optimization and graph theory. The objective is to find the shortest possible route that allows a salesman to visit a given set of cities exactly once and return to the starting city.

### Formal Description

- **Input**: A set of `n` cities and a distance matrix `d(i, j)` representing the distance between each pair of cities `i` and `j`.
- **Output**: A circuit (or cycle) of minimal length that visits each city exactly once and returns to the starting city.

### Applications

The TSP has many practical applications, including:
- Logistics and delivery route planning.
- Printed circuit board design.
- Sales route planning.
- Telecommunications network management.

### Complexity

The TSP is an NP-hard problem, meaning there is no known algorithm to solve it in polynomial time for all cases. However, many heuristic and metaheuristic approaches, such as simulated annealing, genetic algorithms, and ant colony optimization, are used to find approximate solutions in a reasonable amount of time.

### Example

Suppose a salesman needs to visit cities A, B, C, and D. The distances between the cities are given by the following matrix:

|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 10| 15| 20|
| B | 10| 0 | 35| 25|
| C | 15| 35| 0 | 30|
| D | 20| 25| 30| 0 |

The goal is to find the shortest path that visits each city once and returns to the starting city. One possible solution could be A -> B -> D -> C -> A with a total distance of 10 + 25 + 30 + 15 = 80.

### Conclusion

The TSP is a fundamental problem in combinatorial optimization with many practical applications. Although it is difficult to solve exactly for large sets of cities, heuristic approaches allow finding satisfactory solutions within reasonable time frames.