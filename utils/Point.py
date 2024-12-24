import random as rd

class Point:
    def  __init__(self, cord_x: float, cord_y: float):
        self.x, self.y = cord_x, cord_y

    # Calculate the euclidian distance between two points
    def calculateDistanceTo(self, secondPoint: 'Point') -> float:
        """
        Process the euclidian distance between the current instance and another point
        Args:
            secondPoint (Point): another instance of Point
        Returns:
            distance (float): Euclidian distance between the current instance and another point
        """
        return ((self.x - secondPoint.x)**2 +(self.y - secondPoint.y)**2) ** 0.5        
    
    # Update the string representation of a Point as (x, y)
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Update the global representation of a Point as (x, y)
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    # Check if the current Point' instance is similar to a specified one 
    def __eq__(self, secondPoint: 'Point'):
        """
        Overloads the equal operator (to improve unicity)
        Args:
            secondPoint (Point): another instance of Point
        Returns:
            equality (boolean): Whether or not the current instance and second point are identical 
        """
        return self.calculateDistanceTo(secondPoint) == 0

# Generate an instance of Point with random coordinates 
def generateRandomPoint(min: float, max: float, floating_point: int) -> Point:
    """
    Generate an instance of Point by randomizing its coordinates (x, y) with some constraints
    Args:
        min (float): the lower part of the random interval
        max (float): the higher part of the random interval
        floating_point (int): the number of decimal digits
    Returns:
        position (Point): A random point matching all the constraints
    """
    x_cord = round(rd.uniform(min, max), floating_point)
    y_cord = round(rd.uniform(min, max), floating_point)

    return Point(x_cord, y_cord)