# Datos del modelo
tablas = dict()

# Lectura de demandas
demanda_prod = dict()

with open("demanda_productos.csv", "r") as archivo:
    _productos = archivo.readline().strip().split(";")[1:]
    for linea in archivo.readlines():
        dia = linea.strip().split(";")
        demanda_prod[dia[0]] = {i: int(j) for i, j in zip(_productos, dia[1:])}
    tablas["demanda_prod"] = demanda_prod

# Lectura demora de proveedores
llegada_prov = dict()

with open("llegada_proveedores.csv", "r") as archivo:
    _proveedores = archivo.readline().strip().split(";")[1:]
    for linea in archivo.readlines():
        dia = linea.strip().split(";")
        llegada_prov[dia[0]] = {i: int(j) for i, j in zip(_proveedores, dia[1:])}
    tablas["llegada_prov"] = llegada_prov

# Lectura demanda diaria
personas = dict()

with open("llegada_proveedores.csv", "r") as archivo:
    archivo.readline()
    for linea in archivo.readlines():
        dia = linea.strip().split(";")
        personas[dia[0]] = dia[1]
    tablas["personas"] = personas

# Lectura datos adicionales
with open("datos_adicionales.csv", "r") as archivo:
    for linea in archivo.readlines():
        linea = linea.strip().split(";")
        tablas[linea[0]] = linea[1]

# Lectura de tablas

with open("productos.csv") as archivo:
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
    numeros = archivo.readline().strip().split(";")[1:]
    linea = archivo.readline().strip().split(";")
    variable = linea[0]
    while variable:
        tablas[variable] = {i: j for i, j in zip(numeros, linea[1:])}
        linea = archivo.readline().strip().split(";")
        variable = linea[0]

with open("proveedores_productos.csv") as archivo:
    linea = archivo.readline().strip().split(";")
    variable = linea[0]
    proveedor = []
    while variable:
        numeros = archivo.readline().strip().split(";")[1:]
        linea = archivo.readline().strip().split(";")

        mini_diccionario = dict()
        while linea[0] != "":
            if linea[0] not in proveedor:
                proveedor.append(linea[0])
            mini_diccionario[linea[0]] = {i: j for i, j in zip(numeros, linea[1:])}
            linea = archivo.readline().strip().split(";")
        tablas[variable] = mini_diccionario
        linea = archivo.readline().strip().split(";")
        variable = linea[0]


# Dar nombre a diccionarios de productos
proteinas = tablas["proteinas"]
ensaladas = tablas["ensaladas"]
frutas = tablas["frutas"]
vol_prod = tablas["valor_prod"]
inventario_inicial = tablas["inventario_inicial"]
porciones_prod = tablas["porciones_prod"]


# Dar nombre a productos de variables a exportar
productos_diccionario = {**proteinas, **ensaladas, **frutas}
proteinas, ensaladas, frutas = [list(i.keys()) for i in (proteinas, ensaladas, frutas)]
productos = proteinas + ensaladas + frutas


# Dar nombre a tablas de producto/proveedores
periodo_maduracion = tablas["periodo_maduracion"]
periodo_vencer = tablas["periodo_maduracion"]
costo_prod = tablas["costo_prod"]
valor_prod = tablas["valor_prod"]

# Datos adicionales
cap_max = tablas["cap_max"]
presupuesto = tablas["presupuesto"]



'''
print(productos)
print(proteinas, ensaladas, frutas)
print(productos_diccionario)
print(periodo_maduracion)
print(periodo_vencer)
print(cap_max)
print(costo_prod)
print(demanda_prod)
print(presupuesto)
print(vol_prod)
print(valor_prod)
print(llegada_prov)
print(inventario_inicial)
print(personas)
print(porciones_prod)
'''
