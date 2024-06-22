conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print('saque realizado com uso de cheque especial')
    else:
        print('não é possivel realizar o saque')
elif conta_universitaria:
    if saldo >= saque:
        print('saque realizado com sucesso')
    else:
        print("saldo insuficiente")
else:
    print('conta nao reconhecida')