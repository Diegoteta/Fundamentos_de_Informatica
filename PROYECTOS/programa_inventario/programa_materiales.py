menu = ['1.Añadir un nuevo material','2.Buscar material','3.Actualizar stock','4.Filtrar for tipo','5.Calcular valor total','6.Alerta de reabastecimiento','7.Salir']
k='caca'
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
            print(k)
            print('-'*30)
        elif opcion == 2:
            print(k)
            print('-'*30)
        elif opcion == 3:
            print(k)
            print('-'*30)
        elif opcion == 4:
            print(k)
            print('-'*30)
        elif opcion == 5:
            print(k)
            print('-'*30)
        elif opcion == 6:
            print(k)
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
