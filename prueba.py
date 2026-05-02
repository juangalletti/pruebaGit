from functools import lru_cache

class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['id'] = lambda self: hash((self.x, self.y))
        return super().__new__(cls, name, bases, dct)

class Punto(metaclass=Meta):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @lru_cache(None)
    def distancia(self, otro):
        return ((self.x - otro.x)**2 + (self.y - otro.y)**2) ** 0.5

def Y(f):
    return (lambda x: f(lambda *args: x(x)(*args)))(
           lambda x: f(lambda *args: x(x)(*args)))

factorial = Y(lambda f: lambda n: 1 if n == 0 else n * f(n-1))

p1 = Punto(3, 4)
p2 = Punto(0, 0)

print("ID:", p1.id())
print("Distancia:", p1.distancia(p2))
print("Factorial 5:", factorial(5))
