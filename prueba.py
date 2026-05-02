# Variables y tipos de datos
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

# Imprimir en pantalla
print(f"Hola, me llamo {nombre}")
print(f"Tengo {edad} años")

# Operaciones matemáticas
numero1 = 10
numero2 = 5
suma = numero1 + numero2
print(f"Suma: {suma}")

# Condicionales
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Listas
frutas = ["manzana", "plátano", "naranja"]
print(frutas[0])  # Imprime "manzana"

# Bucles
for fruta in frutas:
    print(fruta)

# Funciones
def saludar(nombre):
    return f"¡Hola, {nombre}!"

print(saludar("María"))