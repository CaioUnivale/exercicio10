def calcular_media(lista):
    soma = 0
    for numero in lista:
        soma += numero
    media = soma / len(lista)
    return media
lista_numeros = [10, 20, 30, 40, 50]
media = calcular_media(lista_numeros)
print(f"A média dos números na lista {lista_numeros} é {media}")