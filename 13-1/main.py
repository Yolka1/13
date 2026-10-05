from triangle import Triangle

try:
    triangle = Triangle(3,4,10)

    print("Периметр: ", triangle.perimeter)
    print("Площадь: ", triangle.area)

    print("Угол напротив стороны 3:", triangle.angle(4, 3, 10))
    print("Угол напротив стороны 4:", triangle.angle(3, 10, 4))
    print("Угол напротив стороны 5:", triangle.angle(3, 4, 10))   

except ValueError as error:
    print("Ошибка", error)
    