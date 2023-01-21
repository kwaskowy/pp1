class Areas():
    @staticmethod
    def circle(radius):
        import math
        wynik=math.pi*(radius**2)
        wynik= round(wynik,2)
        print(wynik)
    def triangle(base,height):
        wynik= 0.5*base*height
        print(wynik)
    def rectangle(side1,side2):
        wynik= side1*side2
        print(wynik)


Areas.circle(3)
Areas.triangle(6,2)
Areas.rectangle(3,7)