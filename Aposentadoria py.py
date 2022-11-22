idade = int(input("Digite sua idade"))
tempoContribuido = int(input("Digite o tempo contribuido"))
deficiencia = input("Você possui deficiência?")

if idade >= 60 and tempoContribuido >= 20:
    print("Você pode se aposentar!")
elif idade >= 65 or tempoContribuido >= 25 or deficiencia == "sim":
    print("Você pode se aposentar!")
else:
    print("Você não pode se aposentar!")
