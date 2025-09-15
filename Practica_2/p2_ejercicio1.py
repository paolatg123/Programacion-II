import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, otro):
        return AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def __sub__(self, otro):
        return AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    
    def __mul__(self, otro):
        if type(otro) in [int, float]:
            return AlgebraVectorial(self.x * otro, self.y * otro, self.z * otro)
        else:
            return self.punto(otro)
    
    def __rmul__(self, escalar):
        return self * escalar
    
    def punto(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def cruz(self, otro):
        x = self.y * otro.z - self.z * otro.y
        y = self.z * otro.x - self.x * otro.z
        z = self.x * otro.y - self.y * otro.x
        return AlgebraVectorial(x, y, z)
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def escero(self, valor):
        return abs(valor) == 0
    
    def perpendicular1(self, otro):
        suma = self + otro
        resta = self - otro
        return int(self.escero(suma.magnitud() - resta.magnitud()))
    
    def perpendicular2(self, otro):
        resta1 = self - otro
        resta2 = otro - self
        return int(self.escero(resta1.magnitud() - resta2.magnitud()))
    
    def perpendicular3(self, otro):
        return int(self.escero(self.punto(otro)))
    
    def perpendicular4(self, otro):
        suma = self + otro
        magsuma = suma.magnitud() ** 2
        maga = self.magnitud() ** 2
        magb = otro.magnitud() ** 2
        return int(self.escero(magsuma - (maga + magb)))
    
    def paralela1(self, otro):
        if self.escero(otro.magnitud()):
            return int(self.escero(self.magnitud()))
        
        if self.escero(self.x) == 0 and self.escero(otro.x) == 0:
            r = self.x / otro.x
        elif self.escero(self.y) == 0 and self.escero(otro.y) == 0:
            r = self.y / otro.y
        elif self.escero(self.z) == 0 and self.escero(otro.z) == 0:
            r = self.z / otro.z
        else:
            return int(self.escero(self.x) and self.escero(otro.x) and 
                       self.escero(self.y) and self.escero(otro.y) and 
                       self.escero(self.z) and self.escero(otro.z))
        
        return int(self.escero(self.x - r * otro.x) and
                   self.escero(self.y - r * otro.y) and
                   self.escero(self.z - r * otro.z))
    
    def paralela2(self, otro):
        producto_cruz = self.cruz(otro)
        return int(self.escero(producto_cruz.magnitud()))
    
    def proyeccion(self, otro):
        factor = self.punto(otro) / (otro.magnitud() ** 2)
        return factor * otro
    
    def componente(self, otro):
        return self.punto(otro) / otro.magnitud()


def vectores():
    v1 = AlgebraVectorial(1, 2, 0)
    v2 = AlgebraVectorial(6, 1, 3)
    v3 = AlgebraVectorial(2, 7, 4)
    v4 = AlgebraVectorial(17, 1, 5)
    
    print("Definicion de los vectores: ")
    print(f"Vector a = {v1}")
    print(f"Vector b = {v2}")
    print(f"Vector c = {v3}")
    print(f"Vector d = {v4}")
    print("---------------------------------------------------------")
    
    print("1. DETERMINAR SI DOS VECTORES SON PERPENDICULARES:")
    print(f"a) Si el vector a es ortogonal o perpendicular a b: |a + b| = |a - b|: {v1.perpendicular1(v2)}")
    print(f"b) Si el vector a es mutuamente ortogonal a b: |a - b| = |b - a|: {v1.perpendicular2(v2)}")
    print(f"c) Si el vector a es ortogonal a b: a · b = 0: {v1.perpendicular3(v2)}")
    print(f"d) Si el vector a es ortogonal a b: |a + b|**2 = |a|**2 + |b|**2: {v1.perpendicular4(v2)}")
    print("---------------------------------------------------------")
    
    print("2. DETERMINAR SI DOS VECTORES SON PARALELOS:")
    print(f"e) Si el vector a es paralela a b: a = rb: {v1.paralela1(v3)}")
    print(f"f) Si el vector a es paralela a b: a × b = 0: {v1.paralela2(v3)}")
    print("---------------------------------------------------------")
    
    print("3. DETERMINAR LA PROYECCION DE DOS VECTORES:")
    proyeccion = v4.proyeccion(v1)
    print(f"g) Proyeccion de a sobre b: Proyb a = (a·b/|b|**2)b: {proyeccion}")
    print("---------------------------------------------------------")
    
    print("4. DETERMINAR EL COMPONENTE DE DOS VECTORES:")
    componente = v4.componente(v1)
    print(f"h) Componente de a en b: Compb a = a·b/|b|: {int(componente)}")
    print("---------------------------------------------------------")
if __name__ == "__main__":
    vectores()
