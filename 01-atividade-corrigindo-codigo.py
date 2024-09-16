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

os.system("cls || clear")


# Variáveis para armazenar as estatísticas

QNTD = 5
lista_numeros = []
lista_positivos = []
lista_negativos = []
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0

# Variáveis para armazenar os números
for i in range(QNTD):
    numero = int(input(f"Digite o {i+1}º número: "))

# Def's e o maior/menor

def par_ou_impar():
    lista_numeros = []
    contador_par = 0
    contador_impar = 0
    
    for i in range (6):
        numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        print("\nEsse número é par")
        contador_par += 1
    else:
        print("\nEsse número é impar")
        contador_impar += 1
        lista_numeros.append
        return par_ou_impar  

def positivo_ou_negativo():
    negativos = []
    positivos = []    
    
    if numero < 0:
        negativos.append(numero)
        resultado1 = "Números negativos"
    else:
        positivos.append(numero)
        resultado = "Números negativos"

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

#Processamento
pares, impares = par_ou_impar(lista_numeros)
positivo, negativo = positivo_ou_negativo(lista_numeros)
quantidade_negativos = len(negativo)
soma_negativos = sum(negativo)
quantidade_positivos = len(positivo)
soma_positivos = sum(positivo)
media_pares = contador_par

print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Quantidade de positivos: {positivo}")
print(f"Quantidade de negativos: {negativo}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa: {numeros_invertidos}")