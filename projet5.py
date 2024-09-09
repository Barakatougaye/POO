#Question1
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


my_point = Point3D(1, 2, 3)


print(my_point)  


#Question2
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def area(self):
        return self.longueur * self.largeur

    def perimeter(self):
        return 2 * (self.longueur + self.largeur)


my_rectangle = Rectangle(3, 4)


print("Aire :", my_rectangle.area())  
print("Périmètre :", my_rectangle.perimeter())  


#Question3
import math
class circle:
    def __init__(self, center, radius) :
        self.center= center
        self.radius=radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius  

    def Inside(self, point):
        dist = math.sqrt((point[0] - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2)
        return dist <= self.radius
     
my_circle = circle((1, 1), 4)


print("Aire :", my_circle.area())  
print("Périmètre :", my_circle.circumference())  

print("Le point est-il à l'intérieur ?", my_circle.Inside((4, 6)))



#Question4
