#Kata 4 Ejercicio 2
from matplotlib.pyplot import title

# Datos con los que vas a trabajar
nombre = "Luna"
gravedad = 1.00162 # in kms
planeta = "Tierra"

# Creamos el título
title= f'Datos de la gravedad sobre {nombre}' 

# Creamos la plantilla
hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 """

# Unión de ambas cadenas
template = f"""{title.title()} {hechos} """ 
print(hechos)

# Nuevos datos muestra
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

# Comprobamos la plantilla
print(hechos)

new_template = """
Datos de Gravedad sobre: {nombre}
--------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, 
gravedad=gravedad))

# Pista: print(nueva_plantilla.format(variables))
print(new_template.format(nombre=nombre, planeta=planeta, 
gravedad=gravedad*1000))