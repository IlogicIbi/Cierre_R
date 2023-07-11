cinco = 5
numero_veces = cinco

# Crear una matriz para almacenar las respuestas
respuestas = []

# Pedir al usuario las respuestas y almacenarlas en la matriz
for i in range(numero_veces):
    respuesta = input(f"Ingrese la respuesta {i + 1}: ")  # Pedir al usuario la respuesta
    respuestas.append(respuesta)  # Agregar la respuesta a la matriz

# Mostrar las respuestas por pantalla
for respuesta in respuestas:
    print(respuesta)
