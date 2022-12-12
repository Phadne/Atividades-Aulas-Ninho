# Crie um programa que utilize uma função para comparar o tamanho de 2 palavras.
# Essa função vai receber as 2 palavras, e vai determinar qual das duas
# é a maior e imprimir na tela

palavra = input("insira uma palavra")

while = (True):

    letra = input("insira o caractere")
    if (len(letra) == 1):
        break
    else:
        print("try again!")

print("o caractere '{letra}' na '{palavra}' apareceu '{checagem}' vezes")        

def checarLetra(p,l):
    contador = 0

    for i in range(len(p)):
        if(p[i] == l):
            contador+= 1
    return contador

palavra = input("digite uma palavra:")
letra = input("digite uma letra:")

print(checarLetra(palavra,letra))
