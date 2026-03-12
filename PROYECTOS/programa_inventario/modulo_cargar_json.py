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
def trans_material(diccionario):
    lista=[]
    for elemento in diccionario:
        nuevo_objeto = Material(
            elemento['nombre'], 
            elemento['tipo'], 
            elemento['precio'], 
            elemento['cantidad_stock'])
        lista.append(nuevo_objeto)
    return lista


    



