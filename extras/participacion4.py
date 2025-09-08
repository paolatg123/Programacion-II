import math

class Circulo2D:
    def __init__(self, x=0, y=0, radio=1):
        self.x = x
        self.y = y
        self.radio = radio

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_radio(self):
        return self.radio

    def get_area(self):
        return math.pi * self.radio ** 2

    def get_perimetro(self):
        return 2 * math.pi * self.radio

    def contiene(self, x, y):
        distancia = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return distancia <= self.radio

    def contieneCirculo(self, circulo):
        distancia = math.sqrt((self.x - circulo.x) ** 2 + (self.y - circulo.y) ** 2)
        return distancia + circulo.radio <= self.radio

    def sobrepone(self, circulo) :
        distancia = math.sqrt((self.x - circulo.x) ** 2 + (self.y - circulo.y) ** 2)
        return distancia < self.radio + circulo.radio

    def mostrar(self):
        print(f"Area: {self.get_area():.2f}")
        print(f"Perimetro: {self.get_perimetro():.2f}")
        print(self.contiene(2.5, 0))
        print(self.contieneCirculo(Circulo2D(2, 0, 0.5)))
        print(self.sobrepone(Circulo2D(0, 0, 2)))


if __name__ == "__main__":
    c1 = Circulo2D(2, 0, 1)
    c1.mostrar()
    
