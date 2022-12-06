menuB = 1
num1 = []
par = 0
impar = 0
import os
import random

while menuB == 1:
    menuA = int(input("Lista de Exercicios \n 1-- Quantos numeros são pares? \n 2-- Idades \n 3-- Mercado \n 4-- Notas \n "))
    os.system('cls')
    match menuA:
        case 1:
            for count in range (5):

                num1.append(int(input("Digite o numero\n")))
                os.system('cls')
                
                if num1[count]%2 == 0:
                    par = par+1
                else:
                    impar = impar+1
            print("Você digitou %d numeros pares e %d numeros impares\n" % (par, impar))
            menuB = int(input("\n Deseja Retornar ao Menu? \n 1-- Sim\n 2-- Não"))
            os.system('cls')
        case 2:
            idade = []
            for count in range (5):
                idade.append(int(input("Digite sua idade: \n")))
            print("Maior idade digitada %d" % (max(idade)))
            print("Maior idade digitada %d" % (min(idade)))
            print ("A media das idades é %d" % (sum(idade)/len(idade)))
            menuB = int(input("\n Deseja Retornar ao Menu? \n 1-- Sim\n 2-- Não"))
            os.system('cls')
        case 3:
            produtos = {'Pizza': [20, True], 'Macarrão': [10,False], 'Melancia': [5,True], 'Farofa': [3, False]}
            pesquisa = input("Qual produto deseja comprar? \n Melancia \n Pizza \n Macarrão \n Farofa \n") 
            os.system('cls')

            print(pesquisa, " custa R$ %d"  % (produtos[pesquisa][0]))
            if produtos[pesquisa][1] == True:
                print("E está em estoque")
            else:
                print("E não está em estoque")

            menuB = int(input("\n Deseja Retornar ao Menu? \n 1-- Sim\n 2-- Não"))
            os.system('cls')

        case 4:
            produtos = {'Pablo': [random.sample(range(0,10), 5)], 'Marcela': [random.sample(range(0,10), 5)], 'Fabiana': [random.sample(range(0,10), 5)], 'Maicon': [random.sample(range(0,10), 5)], 'Enzo': [random.sample(range(0,10), 5)]}
            pesquisa = input("Qual Aluno deseja consultar a Nota \n Marcela \n Pablo \n Maicon \n Fabiana \n Enzo \n") 
            os.system('cls')

            print("As notas de %s foram: \n %s " % (pesquisa , produtos[pesquisa]))

            menuB = int(input("\n Deseja Retornar ao Menu? \n 1-- Sim\n 2-- Não"))
            os.system('cls')