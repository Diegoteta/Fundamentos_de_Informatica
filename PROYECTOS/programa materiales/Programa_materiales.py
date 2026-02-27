    #Crear menu 
print('---- ¿ Que quiere hacer ? ----')
print()
menu=['1) Cargar el catálogo desde archivo','2) Listar materiales disponibles','3) Obtener tamaño medio de los materiales'
      ,'4) Obtener tamaño maximo0','5) Obtener tamaño minimo','6) Añadir un nuevo material','7) Editar un material','8) Editar un material existente'
      ,'9) Guardar catalogo a fichero','10) Salir']

nombres=[]
tamaños=[]

for k in menu:
    print(k)

opcion =int(input('Seleccione número para continuar : '))
if opcion>10 or opcion<1:
    opcion =int(input('Seleccione un numero disponible por favor: '))
    
print()
#Opcion 1
if opcion==1:
    
    archivo=input('Seleccione archivo : ')
    with open(archivo,'r') as fichero:
        for linea in fichero:
            lista_limpia = linea.strip().split(',') #limpiamos de huecos
            nombres.append(lista_limpia[0])
            tamaños.append(float(lista_limpia[1]))
    print(f'{nombres} : {tamaños}') 

    

