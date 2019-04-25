
# Datos del modelo

# Lectura de demandas
demandas = dict()

with open("demanda_productos.csv", "r") as archivo:
    productos = archivo.readline().strip().split(";")[1:]
    for linea in archivo.readlines():
        dia = linea.strip().split(";")
        demandas[dia[0]] = {i: int(j) for i, j in zip(productos, dia[1:])}


# Lectura de tablas
with open("tablas.csv") as archivo:
    tablas = dict()
    linea = archivo.readline().strip().split(";")
    variable = linea[0]
    while variable in ["proteinas", "frutas", "ensaladas"]:
        numeros = [i for i in archivo.readline().strip().split(";")[1:] if i != ""]
        nombres = [i for i in archivo.readline().strip().split(";")[1:] if i != ""]
        mini_diccionario = {int(i): j for i, j in zip(numeros, nombres)}
        tablas[variable] = mini_diccionario
        archivo.readline()
        linea = archivo.readline().strip().split(";")
        variable = linea[0]
    while variable != "listo":
        numeros = archivo.readline().strip().split(";")[1:]
        linea = archivo.readline().strip().split(";")
        mini_diccionario = dict()
        while linea[0] != "":
            mini_diccionario[linea[0]] = {int(i): int(j) for i, j in zip(numeros, linea[1:])}
            linea = archivo.readline().strip().split(";")
        tablas[variable] = mini_diccionario
        linea = archivo.readline().strip().split(";")
        variable = linea[0]


# Dar nombre a diccionarios de productos
proteinas = tablas["proteinas"]
ensaladas = tablas["ensaladas"]
frutas = tablas["frutas"]

# Dar nombre a productos de variables a exportar
productos_diccionario = {**proteinas, **ensaladas, **frutas}
proteinas, ensaladas, frutas = [list(i.keys()) for i in (proteinas, ensaladas, frutas)]
productos = proteinas + ensaladas + frutas

# Dar nombre a otras tablas
periodo_maduracion = tablas["periodo_maduracion"]
periodo_vencer = tablas["periodo_maduracion"]


'''
print(demandas)
print(productos)
print(proteinas, ensaladas, frutas)
print(productos_diccionario)
print(periodo_maduracion)
print(periodo_vencer)
'''
