class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def tieneSolucion(self):
        p=(self.a * self.d - self.b * self.c) != 0
        return p

    def getX(self):
        if self.tieneSolucion():
            p=(self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)
            return p
        else:
            return None

    def getY(self):
        if self.tieneSolucion():
            p=(self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)
            return p 
        else:
            return None

def main():
    a, b, c, d, e, f = map(float, input("Ingrese a, b, c, d, e, f: ").split())
    ecuacion = EcuacionLineal(a, b, c, d, e, f)

    if ecuacion.tieneSolucion():
        x = ecuacion.getX()
        y = ecuacion.getY()
        print(f"x = {x}, y = {y}")
    else:
        print("La ecuación no tiene solución")

if __name__ == "__main__":
    main()
