#POO
import math

class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        p=sum(self.datos) / len(self.datos)
        return p

    def desviacion(self):
        media = self.promedio()
        sumaCua = 0
        for x in self.datos:
            sumaCua=sumaCua+ (x - media) ** 2
            c=math.sqrt(sumaCua / (len(self.datos) - 1))
        return c

def main():
    
    datos = list(map(float, input().split()))

    if len(datos) != 10:
        print("No son 10 datos")
        return

    estadistica = Estadistica(datos)
    promedio = estadistica.promedio()
    desviacion = estadistica.desviacion()

    print(f"El promedio es {promedio:.2f}")
    print(f"La desviación estándar es {desviacion:.5f}")

if __name__ == "__main__": 
    main()
