"""
Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de 
seus colegas não concluiu. O Objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida,
mostre na tela:

1. A quantidade de números pares e ímpares.
2. A quantidade de números positivos e negativos.
3. A quantidade de números inseridos.
4. O maior e o menor número.
5. A média dos números pares.
6. A média dos números ímpares.
7. A média de todos os números inseridos.
8. Mostrar os números lidos na ordem inversa.
"""

import os
import time

os.system("cls || clear")


# Variáveis para armazenar as estatísticas

QNTD = 5
list_numero = []
lista_positivos = []
lista_negativos = []

# Variáveis para armazenar os números
for i in range(QNTD):
    numero = float(input(f"Digite o {i+1}º número: "))
    list_numero.append(numero)

# Def's e o maior/menor

def par_ou_impar(n1):
    lista_par = []
    lista_impar = []
    contador_par = 0
    contador_impar = 0
    for numero in n1:
        if numero % 2 == 0:
            contador_par += 1
            lista_par.append(numero)
        else:
            contador_impar += 1
            lista_impar.append(numero)
    return lista_par, lista_impar, contador_par, contador_impar

lista_par, lista_impar, contador_par, contador_impar= par_ou_impar(list_numero)


def positivo_ou_negativo(n2):
    contador_negativos = 0    
    contador_positivos = 0    
    
    for numero in n2:
        if numero <= 0:
            contador_negativos += 1
        else:
            contador_positivos += 1
    return contador_negativos, contador_positivos

contador_negativos, contador_positivos = positivo_ou_negativo(list_numero)

def media(n3):
    QNTD = len(n3)
    soma = sum(n3)
    for numero in n3:
        if numero !=0:
            media = soma/QNTD
            return media
        else:
            return 0

# Processamento
media_par = media(lista_par)
media_impar=media(lista_impar)
media_total=media(list_numero)
maior_numero = max(list_numero)
menor_numero = min(list_numero)
total = len(list_numero)

# Apresentação de dados

f"""\nEstatísticas dos números:
Quantidade de pares: {contador_par}
Quantidade de ímpares: {contador_impar}
Quantidade de positivos: {contador_positivos}
Quantidade de negativos: {contador_negativos}
Maior número: {maior_numero}
Menor número: {menor_numero}
Média dos números pares: {media_par}
Média dos números ímpares: {media_impar}
Média de todos os números: {media_total:.}"""

for i, numero in enumerate (reversed(list_numero)):
    print(f"Total {total-i}º número: {numero}")

time.sleep(1) 