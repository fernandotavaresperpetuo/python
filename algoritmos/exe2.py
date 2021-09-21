id_pesado = int
id_magro = int
id_alto = int
id_baixo = int
id_gordo = 0
id_magro = 0
id_alto = 0
id_baixo = 0
media_altura = float
media_peso = float
media_altura = 0
media_peso = 0
soma_altura = float
soma_peso = float
soma_altura = 0
soma_peso = 0
alto = float
baixo = float
magro = float
gordo = float
alto = 0
baixo = 10
magro = 500
gordo = 0
peso = float
altura = float
soma_codigo = float
soma_codigo = 0
codigo = int
codigo =0
n = 1
while n!= 0:
    codigo = codigo + 1
    altura = 0
    peso = 0
    altura = float(input('digite sua altura: '))
    peso = float(input('digite seu peso: '))
    soma_altura = (soma_altura + altura)
    soma_peso = (soma_peso + peso)
    if alto < altura:
        alto = altura
        id_alto = codigo
    if baixo > altura:
        baixo = altura
        id_baixo = codigo
    if gordo < peso  :
        gordo = peso
        id_gordo = codigo
    if magro > peso:
        magro = peso
        id_magro = codigo

    n = int(input('digite 0 para sair, ou qualquer outro numero para continuar: '))

print('saindo')

print('O mais alto eh o cliente {}, com a altura de {}'.format(id_alto, alto))
print('O mais baixo eh o cliente {}, com a altura de {}'.format(id_baixo, baixo))
print('O mais magro eh o cliente {}, com o peso de {}'.format(id_magro, magro))
print('O mais gordo eh o cliente {}, com a peso de {}'.format(id_gordo, gordo))

media_altura = (soma_altura / codigo)
media_peso = (soma_peso / codigo)

print('A media das altura da: {}'.format(media_altura))
print('A media dos pesos da: {}'.format(media_peso))