import math

class Point2D:
    

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return f"x:{self.x} y:{self.y}"

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"


