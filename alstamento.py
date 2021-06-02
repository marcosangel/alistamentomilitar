from datetime import date
sexo = int(input('Informe seu sexo:\n[1]-masculino\n[2]-feminino\nopção: '))
if sexo == 1:
    atual = date.today().year
    nasc = int(input('Qual o ano de nascimento?: '))
    idade = atual - nasc
    print('Quem nasceu em {}, tem {} anos em {}.'.format(nasc,idade,atual))
    if idade == 18:
        print('voce tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Voce ainda não tem 18 anos. faltam {} anos para se alistar'.format(saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Voce ja deveria se alistado ha {} anos.'.format(saldo))
elif sexo == 2:
    print('Voce não precisa se alistar')
