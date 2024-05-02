# Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde
# en el abecedario y mostrar el nuevo string en pantalla. Por ejemplo:
# Hola → H(8) o(15) l(12) a(1)

import string

def 

#Obtenemos las letras del abecedario
palabra = "Supercalifragilisticoespialidoso"
abecedario = string.ascii_letters[:26]

#Declaramos un diccionario vacío y lo ¿?
dict_letra_a_entero = dict()
for n in range(len(abecedario)):
    dict_letra_a_entero[abecedario[n]] = n

#Con este diccionario se implementa de forma sencilla la lógica de:

for letra in palabra:
    print(letra, )
display = "%s (%s) " * len(palabra)