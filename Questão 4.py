#Resposta Questão 4 Atividade Ciclo 2


numero_primo = int(input("Digite o número: "))


if numero_primo % 2 == 0:
    print(f"Falso número {numero_primo} não é primo")

elif numero_primo / numero_primo == 1 and numero_primo / 1 == numero_primo:
    print(f"Verdadeiro numero {numero_primo} é primo")