# este es el comando para imprimir en consola
""" esta es otra forma de hacer comentarios en varias líneas
como en este ejemplo
y se cierra con comillas dobles 3 veces
"""
print("hola soy yo, mcc")

print (100)
print ("soy nivelpro")

str("test2")

lista = ["string", 1, [1,2,3], "true"]
# definición de listas

{"name": "Carlos"}
# definición de diccionarios

test1 = "Colombia"
# definición de variables
print (test1)
print (lista[3])

def test1():
    return "test"

print(test1())

tupla1 = ("python", "django")
print(tupla1[1])

print(int(5.2))
print(len("estoy en curso de stack"))

print(type(5))
print(sum([5,7,3]))

print(sorted([10,50,25]))

producto = ("carne")
precio = (100)

if (producto == "papas"):
    if (precio >= 50):
        precio = (precio - (precio*10/100))
        print(producto, "a $", int (precio))
elif (producto == "carne"):
     print("por hoy", producto, "gratis")

for i in range(4):
    print(i)

x = 0
while x < 10:
    print (x)
    x +=1