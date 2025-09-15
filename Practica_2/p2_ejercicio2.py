import math

class vector_tridimensional:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def suma(self, otro):
        return vector_tridimensional(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def multi(self, escalar):
        return vector_tridimensional(self.x * escalar, self.y * escalar, self.z * escalar)
    
    def long(self):
        return math.sqrt(int(self.x**2 + self.y**2 + self.z**2))
    
    def normal(self):
        
        m = self.long()
        if m == 0:
            return vector_tridimensional(0, 0, 0)
        return vector_tridimensional(self.x / m, self.y / m, self.z / m)
    
    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def producto_vectorial(self, otro):
        return vector_tridimensional(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )


def vector():
    a = vector_tridimensional(1, 8, 3)
    b = vector_tridimensional(4, 5, 6)
    c = vector_tridimensional(0, 0, 0)  
    
    print("-------------------------------------------------------------")
    print(f"Vector a = {a}")
    print(f"Vector b = {b}")
    print(f"Vector c = {c}")
    print("--------------------------------------------------------------")

    print("a) SUMA: a + b =", a.suma(b))
    print("b) MULTIPLICACIÓN POR ESCALAR: 2 * a =", a.multi(2))
    print("c) LONGITUD: |a| =", a.long())
    print("d) NORMALIZACIÓN: a/|a| =", a.normal())
    print("e) PRODUCTO ESCALAR: a·b =", a.producto_escalar(b))
    print("f) PRODUCTO VECTORIAL: a×b =", a.producto_vectorial(b))
    print(f"a·b = {a.producto_escalar(b)} Son ortogonales? {a.producto_escalar(b) == 0}")
    print(f"a·c = {a.producto_escalar(c)} Son ortogonales? {a.producto_escalar(c) == 0}")
    
if __name__ == "__main__":
    vector()
