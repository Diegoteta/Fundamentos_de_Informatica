import json
class Material:
    def __init__(self,nombre,tipo,precio,cantidad_stock):
        self.nombre=nombre
        self.tipo=tipo
        self.precio=precio
        self.cantidad_stock=cantidad_stock
def abrir_json(ruta):
    with open(ruta,'r',encoding='utf-8') as fichero:
        datos = json.load(fichero)
    return datos
def trans_a_objetos(diccionario):
    lista=[]
    for elemento in diccionario:
        nuevo_objeto = Material(
            elemento['nombre'], 
            elemento['tipo'], 
            float(elemento['precio']), 
            int(elemento['cantidad_stock'])
            )
        lista.append(nuevo_objeto)
    return lista
def trans_a_diccionario(objetos):
    lista=[]
    for elemento in objetos:
        nuevo_diccionario = vars(elemento)
        lista.append(nuevo_diccionario)
    return lista
def comprobacion_existencia(lista,nombre_buscado):
    nombre_minusculas = nombre_buscado.lower()
    for objeto in lista:
        if objeto.nombre.lower() == nombre_minusculas:
            return objeto
    return None
def crear_elemento_inventario(lista,clase):
    n_nombre = input('Nuevo material : ')
    print('-'*30)
    if comprobacion_existencia(lista,n_nombre):
        print(f'El material {n_nombre} ya existe : ')
        print('-'*30)
    else:
        n_tipo = input('Tipo de material : ')
        print('-'*30)
        try:
            n_precio = float(input('Precio : '))
            print('-'*30)
        except:
            print('Use un argumento válido')
            print('-'*30)
            return
        try:
            n_cantidad = int(input('Cantidad : '))
            print('-'*30)
        except:
            print('Use un argumento válido')
            print('-'*30)
            return
        nuevo = clase(n_nombre, n_tipo, n_precio, n_cantidad)
        lista.append(nuevo)
        print(f"Material {n_nombre} añadido con éxito.")
        print('-'*30)
def buscar_material(lista):
    nombre_a_buscar = input('Material que quiere buscar: ')
    encontrado = comprobacion_existencia(lista, nombre_a_buscar)
    if encontrado:
        print(f"\nResultados para: {nombre_a_buscar}")
        for k, v in vars(encontrado).items():
            print(f" > {k.capitalize()}: {v}")
        print('-'*30)
    else:
        print("El material no está en la base de datos.")
        print('-'*30)
def actualizar_stock(lista):
    material_a_actualizar = input('¿De que material quiere modificar el stock? : ')
    print('-'*30)
    objeto_a_modificar = comprobacion_existencia(lista, material_a_actualizar)
    if objeto_a_modificar:
        try:
            variacion = int(input('Modificación de cantidad : '))
            print('-'*30)
            nuevo_stock = objeto_a_modificar.cantidad_stock + variacion
            if nuevo_stock < 0:
                print(f'No hay suficiente stock de {objeto_a_modificar.nombre}')
                print('-'*30)
            else:
                objeto_a_modificar.cantidad_stock = nuevo_stock
                print(f"El nuevo stock es: {objeto_a_modificar.cantidad_stock}")
                print('-'*30)
        except:
            print('Debe de poner un numero entero')
            print('-'*30)
    else:
        print(f'El material {objeto_a_modificar} no consta en la base de datos')
        print('-'*30)
def buscar_tipo(lista, clase):
    resultados = []
    clase_minuscula = clase.lower()
    for objeto in lista:
        if objeto.tipo.lower() == clase_minuscula:
            resultados.append(objeto)
    return resultados
def filtrar_por_tipo(lista):
    tipo_a_buscar = input('Tipo por el que quiere filtrar : ')
    lista_tipo = buscar_tipo(lista,tipo_a_buscar)
    if lista_tipo:
        print(f"\nResultados para tipo : {tipo_a_buscar}")
        print('-'*30)
        for objeto in lista_tipo:
            for k, v in vars(objeto).items():
                print(f" > {k.capitalize()}: {v}")
        print('-'*30)
    else:
        print("No hay materiales clasificados bajo este tipo.")
        print('-'*30)
def coste_total_inventario(lista):
    suma = 0
    for elemento in lista:
        suma += elemento.precio*elemento.cantidad_stock
    return suma
def alerta_abastecimiento(lista):
    try:
        umbral = int(input('Stock mínimo : '))
        print('-' * 30)
        lista_umbral=[]
        for objeto in lista:
            if objeto.cantidad_stock < umbral:
                lista_umbral.append(objeto)
        if len(lista_umbral) == 0:
            print('No hace falta reponer material')
            print('-' * 30)
        else:
            print(f'--- REPONER STOCK // Inferior a {umbral}uds ---')
            print('-' * 30)
            for objeto in lista_umbral:
                for k, v in vars(objeto).items():
                    print(f" > {k.capitalize()}: {v}")
                print('-' * 30)
    except:
        print('Use un atgumento válido')
        print('-' * 30)



