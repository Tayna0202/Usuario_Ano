print("------------------------------------------")

nomeCompleto = (input("Digite seu nome completo: "))

ano = int (input("Digite seu ano de nascimento: "))

while(ano < 1922 or ano > 2021):
    ano = int (input("Ano digitado errado, digite novamente: "))

print("Nome completo: ", nomeCompleto)
print("Ano de nascimento: ", ano)