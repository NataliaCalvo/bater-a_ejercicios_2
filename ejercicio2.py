# Imaginemos que en nuestra tienda hay un carné por puntos y que alguien debe pagar el
# precio_final_de_compra. Si tienes menos de 100 puntos realizaremos un descuento del
# 10%. Si es mayor a 100 y menor a 150 aplicamos un 12%. Si tienes 150 un 15% y sino, el
# resto de los casos de más de 150, un 20%.
# Crea una función que reciba el precio incial de la compra y el número de puntos del
# comprador y que devuelva el precio final que este debe pagar.

def precio_final_de_compra(inicial, puntos):
    if puntos < 100:
        descuento = 0.1
    elif puntos > 100 and puntos < 150:
        descuento = 0.12
    elif puntos == 150:
        descuento = 0.15
    else: descuento = 0.2

    precio_final = inicial * (1 - descuento)
    return precio_final

inicial = 200
puntos = 120
precio_final = precio_final_de_compra(inicial, puntos)

print("El precio final con descuento es de: ", precio_final)