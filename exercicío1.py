# Escreva a função que, dado o valor da conta
# de um restaurante, calcule e exiba a gorjeta
# do garçom,considerndo 10% do valor da conta
#def gorjetaGarcom(valorConta):
 #gorjeta= valorConta*0.1
 #return gorjeta#

#valorGorjeta = gorjetaGarcom(300)
#print(valorGorjeta)



def soma(n1, n2):
    return float(n1) + float(n2)

def subtracao(n1, n2):
    return float(n1) - float(n2)

def multiplicacao(n1, n2):
    return float(n1) * float(n2)

def divisao(n1, n2):
     return float(n1) / float(n2)
  
def calculator(n1,n2,op):

    if op == "+":
        print(soma(n1,n2))

    elif op == "-":
         print(subtracao(n1,n2))

    elif op  == "*":
         print(multiplicacao(n1,n2))

    elif op == "/":
        print(divisao(n1,n2))

    else:
         print("try again!")

# operador = input("Escolha(+,-,*,/)")

# if operador == "+":
#     print(soma(num1,num2))

#elif operador == "-":
    #print(subtracao(num1,num2))

#elif operador == "*":
    #print(multiplicacao(num1,num2))#

#elif operador == "/":
    #print(divisao(num1,num2))#

#else:
    #print("try again!")

num1= input("Escreva o número 1:")
num2= input("Escreva o número 2:")

operator = input("Escolha(+,-,*,/)")
if(num1.isnumeric()) and (num2.isnumeric()):
    calculator(num1,num2,operator)

