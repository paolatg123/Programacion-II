import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.vidasIniciales = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas

    def quitaVida(self):
        if self.numeroDeVidas > 0:
            self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina el NUMERO entre el 0 y el 10.")

        while True:
            try:
                intento = int(input())
                if intento < 0 or intento > 10:
                    print("El numero ingresado SOBREPASO EL RANGO ASIGNADO, PORFA INGRESE OTRO NUMERO")
                    continue
                if intento == self.numeroAAdivinar:
                    print("ACERTASTE!!")
                    self.actualizaRecord()
                    break
                else:
                    quedanVidas = self.quitaVida()
                    if quedanVidas:
                        if intento < self.numeroAAdivinar:
                            print("El numero a adivinar es mayor. Vuelva a ingresar el numero.")
                        else:
                            print("El numero a adivinar es menor. Vuelva a ingresar el numero.")
                    else:
                        break
            except ValueError:
                print("El numero ingresado SOBREPASO EL RANGO ASIGNADO, PORFA INGRESE OTRO NUMERO")
                continue
            

if __name__ == "__main__":
    juego = JuegoAdivinaNumero(3)
    juego.juega()
