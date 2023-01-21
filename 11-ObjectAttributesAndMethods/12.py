class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    @staticmethod
    def distance(p1, p2):
        import math
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

p1 = Point(1, 2)
p2 = Point(3, 4)

if p1 == p2:
    print("The distance between the points is 0.")
else:
    print("The distance between the points is ", Point.distance(p1, p2))
