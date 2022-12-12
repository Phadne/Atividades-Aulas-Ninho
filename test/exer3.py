
if (operador == "+" or operador.lower() == "somar") :
        
        print("A soma dos valores é: ",num1+num2)

    elif(operador == "-" or operador.lower() == "subtrair") :
        
        print("A subtração dos valores é: ",num1-num2)

        elif(operador == "/" or operador.lower() == "dividir") :
         
        if(num2==0):
            repetir=True
            print("Número inválido")
        else:
            print("A divisão dos valores é: ",num1/num2)

    elif(operador == "*"  or operador.lower() == "multiplicação") :
        
        print("A multiplicação dos valores é: ",num1*num2)

    else:
        repetir= True
        print("O operador que você digitou é inválido!")    
