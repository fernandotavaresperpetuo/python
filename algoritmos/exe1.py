numero = float(input('digite um numero: '))
print('\n')
print('digite 1 - a.par ou impar\n')
print('digite 2 - b.positivo ou negativo\n')
print('digite 3 - c.inteiro ou decimal\n')
escolha = int(input('digite o numero correspondente a sua opção: '))
print('\n')


if  (escolha == 1):
    if  (numero % 2 == 0):
        print('o numero {} é par'.format(numero))
    else:
        print('o numero {} é impar'.format(numero))

if  (escolha == 2):
        if  numero > 0:
                print('numero {} eh positivo'.format(numero))
        else:
            if numero < 0:
                print('numero {} eh negativo'.format(numero))

if (escolha == 3):
    if (numero // 1 == numero):
        print('\nNúmero inteiro !')
    else:
        print('\nNúmero Decimal !')