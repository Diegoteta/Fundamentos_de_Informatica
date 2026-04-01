#Este código fue hecho por Alejandro Álvarez Vázquez y Diego Suárez Ladero
import modulo_cargar_json as f
menu = ['1.Añadir un nuevo material','2.Buscar material','3.Actualizar stock','4.Filtrar for tipo','5.Calcular valor total','6.Alerta de reabastecimiento','7.Salir']
datos_crudos = f.abrir_json(r"C:\Users\Pc\Documents\UNI\2º-Cuatri\Fundamentos de Informática\RepositorioFundamentosInformatica\PROYECTOS\programa_inventario\inventario.json")
inventario = f.trans_a_objetos(datos_crudos)
continua = True
while continua :
    print('SISTEMA DE GESTIÓN DE LABORATORIO'); print('-'*30)
    for n in menu:
            print(n) 
    print('-'*30)
    try :
        opcion = int(input('Seleccione una opción : '))
        print('-'*30)
        if opcion == 1:
            f.crear_elemento_inventario(inventario,f.Material)
            print('-'*30)
        elif opcion == 2:
            f.buscar_material(inventario)
            print('-'*30)
        elif opcion == 3:
            f.actualizar_stock(inventario)
            print('-'*30)
        elif opcion == 4:
            f.filtrar_por_tipo(inventario)
            print('-'*30)
        elif opcion == 5:
            suma = f.coste_total_inventario(inventario); print(f'El valor total del imventario es de {suma}€')
            print('-'*30)
        elif opcion == 6:
            f.alerta_abastecimiento(inventario)
            print('-'*30)
        elif opcion == 7:
            continua = False
            print('Saliendo...')
            print('-'*30)
        else:
            print('Use un numero fuera de rango')
            print('-'*30)
    except:
        print('Use un argumento válido')
        print('-'*30)
