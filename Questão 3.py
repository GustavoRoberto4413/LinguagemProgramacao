#Resposta Questão 3 Atividade Ciclo 2

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
terceiro_numero = int(input("Digite o terceiro numero: "))

menor_numero = primeiro_numero

if (segundo_numero < menor_numero):
    menor_numero = segundo_numero

if (terceiro_numero < menor_numero):
    menor_numero = terceiro_numero


print("Menor numero é: ",menor_numero)