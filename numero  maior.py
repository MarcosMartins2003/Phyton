valor = 1
maior = 0
menor = 0
total = 0
quant = 0
import os 

while total >= -1:
    valor = int (input("Digite um Numero \n"))
    quant = quant+1
    os.system('cls')
    total = (total + valor) / quant
    int(total)
    print("A media dos seus numeros é:  %s" %total)
    #Sprint (maior)
    
