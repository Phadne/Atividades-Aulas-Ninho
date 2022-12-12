
def checarInteiro(n): 
    if(num.isnumeric()):
        print("Show")
        global repetir
        repetir = False
    else:
        print("Try again")
        print("iNVÁLIDO")

repetir = True

while(repetir):
    num= (input("Digite um número inteiro:"))
    checarInteiro(num)
    