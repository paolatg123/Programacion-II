#program modular
import math

def promedio(datos):
    return sum(datos) / len(datos)

def desviacion(datos):
    media = promedio(datos)
    sumaCua = 0
    for x in datos:
        sumaCua=sumaCua+ (x - media) ** 2
        c=math.sqrt(sumaCua / (len(datos) - 1))
    return c

def main():
    
    datos = list(map(float, input().split()))

    if len(datos) != 10:
        print("No son 10 datos")
        return

    prom = promedio(datos)
    desv = desviacion(datos)

    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desv:.5f}")

if __name__ == "__main__": 
    main()
