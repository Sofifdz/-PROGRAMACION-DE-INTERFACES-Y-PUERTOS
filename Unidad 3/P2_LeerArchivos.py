def cargar_archivo():
    archivo = open("../Unidad 3/Archivos/ejemplo.csv")

    contenidoArchivo = archivo.readlines()
    #print(contenidoArchivo)

    #------------------------------------------------------------------------------------------

    #convertirlo a lista

    lineas = [ i.split(",") for i in contenidoArchivo]
    #print(lineas)

    #quitar \n
    lineas = [i[0:-2].split(",") for i in contenidoArchivo]
    #print(lineas)
    #------------------------------------------------------------------------------------------

    #quitar comillas en numero

    '''for elemento in lineas:
        elemento[-1] = int(elemento[-1])
    
    print(lineas)'''


    '''lineas = [[i[0], int (i[1])] for i in lineas]
    print("Nueva lista",lineas)'''


    ListaNueva=[]
    for i in lineas:
        ListaNueva.append([i[0],int(i[1])])
    #print(ListaNueva)

    return ListaNueva

a = cargar_archivo()
print(a)
