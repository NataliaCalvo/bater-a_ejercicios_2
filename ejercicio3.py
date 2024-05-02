# Debemos crear una función para calcular la tarifa a pagar por los usuarios de un
# polideportivo. La función recibe la tarifa anual total (100%), la edad del usuario y su
# situación laboral. La tarifa final se calcula en base al criterio siguiente:
# 1. Criterio 1: Si es mayor de edad y está trabajando -> Paga el 100%
# 2. Criterio 2: Si es menor de edad y está trabajando -> Paga el 95%
# 3. Criterio 3: Si es mayor de edad y no está trabajando -> Paga el 75%
# 4. Criterio 4: Si es menor de edad y no está trabajando -> Paga el 50%
# Probar diferentes configuraciones de usuario y tarifas y ver como afectan estos a la tarifa
# final.

def tarifa_final(tarifa_total, edad, trabajando):
    if edad >= 18:
        if trabajando:
            tarifa_final=tarifa_total
        else: 
            tarifa_final = tarifa_total * 0.75
    else:
        if trabajando:
            tarifa_final=tarifa_total *0.95
        else:
            tarifa_final=tarifa_total *0.50
    return tarifa_final

tarifa_total = 100
edad = 16
trabajando = False

print(tarifa_final(tarifa_total, edad, trabajando))



