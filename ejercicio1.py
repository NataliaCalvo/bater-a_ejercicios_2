#1. Crear una función donde se implemente el siguiente algoritmo que permite calcular si un año es bisiesto:
#1. Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
#2. Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
#3. Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
#4. El año es un año bisiesto (tiene 366 días).
#5. El año no es un año bisiesto (tiene 365 días).
#Probar con varios años que la función funciona de manera correcta.

def bisiesto(ano_bisiesto):
    if ano_bisiesto % 4 == 0 and (ano_bisiesto % 100 != 0 or ano_bisiesto % 400 == 0):
                return True
    else:
                return False
            
anos_de_prueba = [2001, 2010, 2022, 1995, 1983, 2024]            
            
for ano_bisiesto in anos_de_prueba:
    if bisiesto(ano_bisiesto):
        print(f"{ano_bisiesto} es un año bisiesto.")
    else:
        print(f"{ano_bisiesto} no es un año bisiesto.")