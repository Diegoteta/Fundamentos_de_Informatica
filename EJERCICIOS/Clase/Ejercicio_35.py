numeros = [2,5,8,9]
#suma
suma = sum(numeros); print(suma)
print()
#¿8?
for n in numeros:
    if n == 8:
        print('Está el 8')
        break
print()
#multiplo de 4
for n in numeros:
    if n%4 ==0 :
        print('Esta multiplo de 4')
        break
print()
#muestre los impares
for n in numeros:
    if n%2 != 0 :
        print(n)
#nueva lista con pares
nueva = []
for n in numeros:
    if n%2 == 0 :
        nueva.append(n)
print(nueva)



if len(numeros)%2 == 0:
    for i in range(0,len(numeros),2):
        print(numeros[i]+numeros[i+1])

    


        

