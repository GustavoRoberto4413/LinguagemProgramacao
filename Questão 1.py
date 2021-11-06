

dias_nascimento = int(input("Digite a idade em dias: "))

ano = (dias_nascimento / 365)
mes = (dias_nascimento % 365) / 30
dia = (dias_nascimento % 365) % 30

print("A idade em anos é: %.0f " % ano)
print("A idade em meses é: %.0f " % mes)
print("A idade em dias é: %.0f " % dia)

print('A idade em anos, meses e dias é %.0f %.0f %.0f '% (ano, mes, dia))