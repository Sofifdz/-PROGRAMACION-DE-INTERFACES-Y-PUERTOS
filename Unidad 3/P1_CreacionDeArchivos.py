
archivo = open("../Unidad 3/Archivos/ejemplo.csv","w")

#si el archivo no existe lo crea,si existe lo sobreescribe

listaNombres =[
    ["Clemente",26],
    ["Cristobal",17],
    ["Ana",5],
    ["Rene",30],
    ["Orozco",8],
    ["Jorge",72],
    ["Aquino",13],
    ["Badillo",37],
    ["Segoviano",40],
    ["Salazar",75],
    ["Eduardo",18],
    ["Natalia",12],
    ["Rodrigo",11],
    ["Miguel",99],
    ["Amando",5],
    ["Raul",6],
    ["Lexis",3],
    ["Mariana",33],
    ["Angel",10],
    ["Emmanuel",51],
    ["Isaac",70],
    ["Paniagua",82],
    ["Sergio",85]
]

print(listaNombres)

#primero se ejecuta este
'''for nombre in listaNombres:
    archivo.write(nombre + "\n")'''
#luego este
for datosNombre in listaNombres:
    for dato in datosNombre:
        archivo.write(str(dato) + ",")
    archivo.write("\n")
archivo.flush()
archivo.close()