def abrir_archivo(ruta):
   
    try: #ahorramos q se rompa si introducimos un archivo q no exista
        with open(ruta,'r') as fichero:
            nombres.clear() #limpiamos si abrimos archivo
            tamaños.clear()
            for linea in fichero:
                lista_limpia = []
                lista_limpia = linea.strip().split(',') #limpiamos de huecos
                nombres.append(lista_limpia[0])
                tamaños.append(float(lista_limpia[1]))        
    except:
        print('Asegurese de que el archivo existe o esta bien escrito.')
def listar_materiales(nombres,tamaños):
    print('-'*30)
    print(f"{'MATERIALES':<15} | {'TAMAÑO':<15}") #guardamos15 huecos para los no,bres y 10 para los tamaños y los dividimos con una ralla
    print('-'*30)
def media_de_lista(lista):
    media = sum(lista)/len(lista)
    print('-'*30)
    print('Tamaño medio de materiales : ',media)
    print('-'*30)
def numero_max(nombres,numeros):
    nombres_numeros = zip(nombres,numeros)
    numeros_maximo = max(nombres_numeros,key=extraer_numero) #le decimos q compare la columna 1 (numeros) para elegir el maximo
    return print(f"El más grande es {numeros_maximo[0]} con un tamaño de {numeros_maximo[1]}")
def numero_min(nombres,numeros):
    nombres_numeros = zip(nombres,numeros)
    numeros_minimo = min(nombres_numeros,key=extraer_numero) #le decimos q compare la columna 1 (numeros) para elegir el maximo
    return print(f"El más pequeño es {numeros_minimo[0]} con un tamaño de {numeros_minimo[1]}")
def extraer_numero(numero): # creamos una funcion para sacar el numero de cada par de datos
                return numero[1]
def add_nuevo_material(nombres,numeros):
    nuevo = input('Nuevo material : ')
    nombres_minusculas = [n.lower() for n in nombres]

    if nuevo.lower() in nombres_minusculas:
        print(f"Error: El material '{nuevo}' ya existe en la lista.")
    else:
        nombres.append(nuevo)
        numeros.append(input('Tamaño : '))
        print(f"{'MATERIALES':<15} | {'TAMAÑO':<15}") #guardamos15 huecos para los no,bres y 10 para los tamaños y los dividimos con una ralla
        print('-'*30)
        for i in range(len(nombres)):
            print(f"{nombres[i]:<15} | {numeros[i]:<10}")          
def editacion(lista_a_editar): #no hace falta un return para actualizar la lista, ya ocurre en la propia funcion
    nombre_editar = input('Escriba el material a cambiar el tamaño : ')
                
    encontrado = False #comprobamos la exitencia del material
    for elemento in lista_a_editar:
        if elemento[0].lower() == nombre_editar.lower(): #.lower para que den inguales mayusculs o minusculas
            try:
                nuevo_tamaño = float(input(f"Nuevo tamaño para {elemento[0]} : "))
                elemento[1] = nuevo_tamaño
                print('-'*30) 
                print(f"El nuevo tamaño de {elemento[0]} es {elemento[1]}")
                print('-'*30) 
                encontrado = True
                break #se cumple el q lo ha encontrado y acaba el bucle
            except:
                print('-'*30) 
                print('Introduzca un valor válido')
                print('-'*30) 
                return #en el caso de error corta la funcion y te saca de ella
    if not encontrado: #si se sigue cumpliendo encontrado=false en todos los elementos,se ejcuta esto
        print('-'*30) 
        print('No se encontró el material')
        print('-'*30)
def conversion_dos_listas_una_lista(nombres,numeros):
    lista_a_editar = []
    for i in range(len(nombres)):
        lista_a_editar.append([nombres[i],numeros[i]])
    return lista_a_editar
def conversion_una_lista_dos_listas(lista_a_editar):
    nombres[:],tamaños[:] = zip(*lista_a_editar) #desempaquetamos para q se actualicen las listas, el asterisco hace q separe la lista datos como dos sublistas datos[0],datos[1]
    print('-'*30) 
    for i in range(len(nombres)):
        print(f"{nombres[i]:<15} | {tamaños[i]:<10}")
    print('-'*30)
def guardar_archivo(nombre_archivo,nombres,tamaños):
                try:
                    with open(nombre_archivo,'w') as f:
                        f.write(f"{'NOMBRES':<15} | {'TAMAÑOS':<10}\n")
                        for i in range(len(nombres)):
                            f.write(f"{nombres[i]:<15} | {tamaños[i]:<10}\n")
                    print('-'*30) 
                    print(f"Cambios guardados en {nombre_archivo}")
                    print('-'*30) 
                except Exception as e: #le indicas q cualquier error (e) te lo imprima luego
                    print('-'*30) 
                    print(f"ERROR : {e} ")
                    print('-'*30) 