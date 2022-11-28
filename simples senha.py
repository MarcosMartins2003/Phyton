senha = "545123456"
tentativas = 5
while senha != "123456" and tentativas>0:
    senha = str(input("Digite sua Senha"))
    tentativas = tentativas - 1
    print("Tentativas Restantes: \n", tentativas)

if tentativas <= 0:
    "Ja era pra ti"
    senha = "123456"
else:
    print ("Acesso consedido :)")


