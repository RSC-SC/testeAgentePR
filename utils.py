def calcular_media(notas):
    total = 0
    for i in range(len(notas)):
        total = total + notas[i]
    return total / len(notas)