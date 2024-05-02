# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
# ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
# informando de ello.
# Fruta Precio
# Plátano 1.35
# Manzana 0.80
# Pera 0.85
# Naranja 0.70

precios_frutas = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

fruta = input("Introduce el nombre de la fruta: ")
kilos = float(input("Introduce la cantidad en kilos: "))

if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print("El precio de", kilos, "kilos de", fruta, "es:", precio_total)
else:
    print("Lo siento, la fruta", fruta, "no está en el diccionario de precios.")
