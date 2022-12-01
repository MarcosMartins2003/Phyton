menuB = 1
import os

while menuB == 1:
    menuA = int(input(" Qual operação deseja realizar ?\n1-- Soma\n2-- Subtração\n3-- Divisão\n4-- Multiplicação\n5-- Fatorial\n6-- Porcentagem de impares"))
    os.system('cls')
    match menuA:
        case 1:
            num = int(input("Diigte um numero de 1 a 10"))
            if num < 1  or num > 10:
                print("Seu numero é invalido")
                menuB = 1
                os.system('cls')
            else:
                for cont in range(10):
                    print( "%d + %d = %d" % (num, cont+1, num+(cont+1)))
            
            menuB = int(input("Deseja voltar ao menu? \n1-- Sim\n2-- Não"))
            os.system('cls')
        case 2:
            num = int(input("Diigte um numero de 1 a 10"))
            if num < 1  or num > 10:
                print("Seu numero é invalido")
                menuB = 1
                os.system('cls')
            else:
                for cont in range(10):
                    print( "%d - %d = %d" % (num, cont+1, num-(cont+1)))
            menuB = int(input("Deseja voltar ao menu? \n1-- Sim\n2-- Não"))
            os.system('cls')
        case 3:
            num = float(input("Diigte um numero de 1 a 10"))
            if num < 1  or num > 10:
                print("Seu numero é invalido")
                menuB = 1
                os.system('cls')
            else:
                for cont in range(10):
                    print( "%d / %d = %d" % (num, cont+1, num/(cont+1)))
            menuB = int(input("Deseja voltar ao menu? \n1-- Sim\n2-- Não"))
            os.system('cls')
        case 4:
            num = int(input("Diigte um numero de 1 a 10"))
            if num < 1  or num > 10:
                print("Seu numero é invalido")
                menuB = 1
                os.system('cls')
            else:
                for cont in range(10):
                    print( "%d X %d = %d" % (num, cont+1, num*(cont+1)))
            menuB = int(input("Deseja voltar ao menu? \n1-- Sim\n2-- Não"))
            os.system('cls')
        case 5:
            result = 1
            fatorial = int ( input("Digite um numero"))
            for cont in range (1,fatorial+1):
                result *= cont    
                print (result)
            menuB = int(input("Deseja voltar ao menu? \n1-- Sim\n2-- Não"))
            os.system('cls')
        case 6:
            par = 0
            impar = 0
            result = 0
            for cont in range (10):
                 num = int(input("Digite o %d numero" % (cont+1)))
                 if (num%2) == 0:
                    par = par + 1
                 else:
                    impar = impar + 1
            result = (((par+impar) - impar)/(par+impar))*100
            print("A porcentagem de numeros impares é de: %d" % result)
            menuB = int(input("Deseja voltar ao menu? \n1-- Sim\n2-- Não \n"))
            os.system('cls')

        
                