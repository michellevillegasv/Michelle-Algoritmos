radio=int(input("Enter the ratio of the circle: "))
altura = int(input("Enter the altura of the cilindro: "))
def area_circle(radio,pi=3.1416):
    area_circle = ((radio)**2)*pi
    return area_circle
area_circle1 = area_circle(radio)
def volumen_cilindro(area_circle,altura):
    volumen = area_circle*altura
    return volumen
print(f"The area of the circle is {area_circle1} and the volume of the cilindro is {volumen_cilindro(area_circle1,altura)}")
