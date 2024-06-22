MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

# if idade >= MAIOR_IDADE:
#     print("Pode tirar CNH")

# if idade < MAIOR_IDADE:
#     print('Não pode tirar CNH')

if idade >= MAIOR_IDADE:
    print("Pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas mas não práticas")
else:
    print("Não pode tirar CNH")