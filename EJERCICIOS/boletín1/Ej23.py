peticion = input('Introduce número entre 1 y 12 :')

numero_valido = False
while not numero_valido:
    if peticion.isnumeric():
        numero = int(peticion)
        if numero < 1 or numero > 12:
            peticion = input('Introduce un numero entre 1 y 12 :')
        else:
            numero_valido = True
    else:
        peticion = input('Introduce un numero entre 1 y 12 :')
print('El numero es :',numero)