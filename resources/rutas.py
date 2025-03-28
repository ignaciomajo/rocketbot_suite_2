from pathlib import Path

path = "C:/Users/Ignacio/OneDrive/Documents/git-and-github/rocketbot_suite_2/rocketbot_suite_2/resources/rutas.txt"
path = Path(path)

with open(path, "r") as f:
    rutas = f.read().strip().split("\n")

print(rutas)

lista_archivos_articulos = []

for ruta in rutas:
    if 'articulos' in ruta:
        ruta = ruta.replace("\\", "/").strip()
        lista_archivos_articulos.append(ruta)

print(lista_archivos_articulos)


for archivo in lista_archivos_articulos:
    if 'xml' in archivo:
        path = "C:/Users/Ignacio/OneDrive/Documents/git-and-github/rocketbot_suite_2/rocketbot_suite_2/resources/ruta_xml.txt"
        path = Path(path)
        with open(path, "w") as f:
            f.write(archivo)
    else:
        path = "C:/Users/Ignacio/OneDrive/Documents/git-and-github/rocketbot_suite_2/rocketbot_suite_2/resources/ruta_xlsx.txt"
        path = Path(path)
        with open(path, "w") as f:
            f.write(archivo)
