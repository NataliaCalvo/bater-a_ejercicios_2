# Crear una lista la cual almacene 10 números positivos ingresados por el usuario, mostrar en
# pantalla: la suma de todos los números, el promedio, el número mayor y el número menor.
# Función para validar si un número es positivo
count = 0

lista_de_numeros = []
while count < 10:
    numero = int(input("Escriba un número (se le pedirá que haga este paso 10 veces): "))
    if numero > 0:
        lista_de_numeros.append(numero)
        count += 1
    else:
        print("Por favor, escriba un número positivo.")

suma_total = sum(lista_de_numeros)
promedio = suma_total / len (lista_de_numeros)
numero_mayor = max(lista_de_numeros)
numero_menor = min(lista_de_numeros)

print("La suma de todos los números es", suma_total)
print("El promedio es:", promedio)
print("El número mayor es:", numero_mayor)
print("El número menor es:", numero_menor)