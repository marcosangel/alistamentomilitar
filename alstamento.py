from datetime import date

def IdadeValida(i):
    if(i >= 0):
      return True
def AnalisarIdadeParaAlistamento():
    atual = date.today().year
    nasc = int(input('Qual o ano de nascimento?: '))
    idadeParaAlistamento = 18; 
    idade = atual - nasc
    if(IdadeValida(idade)):            
        print('Quem nasceu em {}, tem {} anos em {}.'.format(nasc,idade,atual))
        if idade == idadeParaAlistamento:
            print('voce tem que se alistar IMEDIATAMENTE!')
        elif idade < idadeParaAlistamento:
            saldo = idadeParaAlistamento - idade
            print('Voce ainda não tem 18 anos. faltam {} anos para se alistar'.format(saldo))
        elif idade > idadeParaAlistamento:
            saldo = idade - idadeParaAlistamento
            print('Voce ja deveria se alistado ha {} anos.'.format(saldo))
    else:
         print("A sua idade não é válida")        

#Inicio da análise 
sexo = int(input('Informe o seu sexo:\n[1]masculino\n[2]feminino\nopção: '))        
if(sexo == 1):
    AnalisarIdadeParaAlistamento()
else :    
    print("Mulher não vale")

