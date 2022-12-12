def soma (numero1,numero2):
    return float(numero1) + float(numero2)

def subtracao (numero1,numero2):    
    return float(numero1) - float(numero2)

def multiplicacao (numero1,numero2):
    return float(numero1) * float(numero2)
   
def divisao(numero1,numero2):
    if(numero2 == "0"):
        global repetir
        repetir = True
        return " O número 2 não pode ser zero"   
    else:
        return float(numero1) / float(numero2)

def calculadora(n1,n2,op):

    if (op == "+" ) :

        print("A soma dos valores é: ",n1+n2)
    elif(op == "-" ) :

        print("A subtração dos valores é: ",n1-n2)

    elif(op == "/") :
    
        if(n2==0):
            global repetir
            repetir=True
            print("Número inválido")
        else:
            print("A divisão dos valores é: ",n1/n2)

    elif(op == "*" ) :

        print("A multiplicação dos valores é: ",n1*n2)

    else:
        print("O operador que você digitou é inválido!")
        global repetir
        repetir = True
        
        
repetir= True

while(repetir):

    repetir = False
    num1 = float(input("Digite o primeiro número:"))

    num2 = float(input("Digite o segundo valor"))

    operador = input("Digite a operação (+,-,/,*): ")

    calculadora(num1,num2,operador)

