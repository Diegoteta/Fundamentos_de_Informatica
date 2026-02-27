numero_de_filas=int(input('Numero de filas '))
filas=''
a=0
b=0
while a<numero_de_filas:
    filas+='*'
    a+=1
    print(filas)
print()


filas = int(input('Numero de filas '))
for i in range(1, filas + 1):
    c=0
    for j in range(i):
        c+=1
        print(c, end="")
    print()
