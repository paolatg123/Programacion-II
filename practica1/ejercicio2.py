import math

class EcuacionLineal:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        discriminante = self.b**2 - 4 * self.a * self.c
        return discriminante

    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            return raiz1
        elif discriminante == 0:
            raiz1 = -self.b / (2 * self.a)
            return raiz1
        else:
            return 0

    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if discriminante > 0:
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return raiz2
        elif discriminante == 0:
            return None
        else:
            return 0

def main():

    
    a, b, c = map(float, input("Ingrese a,b,c: ").split())

    ecuacion = EcuacionLineal(a, b, c)
    discriminante = ecuacion.getDiscriminante()

    if discriminante > 0:
        raiz1 = ecuacion.getRaiz1()
        raiz2 = ecuacion.getRaiz2()
        print(f"Las raíces son: r1 = {raiz1:.6f} y r2 = {raiz2:.5f}")
    elif discriminante == 0:
        raiz = ecuacion.getRaiz1()
        print(f"La raíz única es: r = {raiz:.0f}")
    else:
        print("La ecuación no tiene raíces reales.")

if __name__ == "__main__":
    main()
