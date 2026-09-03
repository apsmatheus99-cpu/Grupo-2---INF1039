def calcula_divisão(x,y):
    return (x/y)

def calcula_multiplicacao(x, y):
    return (x * y)

def calcula_subtracao(x, y):
    return (x - y)

def calcula_soma(x,y):
    return (x+y)


print('Escolha uma das opções abaixo: ')      
print('1 - Adição')  
print('2 - Subtração')  
print('3 - Multiplicação')  
print('4 - Divisão')
print('(...)')
print('0 - Sair do programa')  

x = float(input('Digite o número: '))
y = float(input('Digite o número: '))
nome_da_operacao= input("Digite a função: ")
while nome_da_operacao != '0':
    if nome_da_operacao == '1':
        resultado = calcula_soma(x, y)
        print(resultado)
    elif nome_da_operacao == '2':
        resultado = calcula_subtracao(x, y)
        print(resultado)
    elif nome_da_operacao == '3':
        resultado = calcula_multiplicacao(x, y)
        print(resultado)
    elif nome_da_operacao == '4'and y != 0:
        resultado = calcula_divisão(x, y)
        print(resultado)
    else: 
        print('Operação invalida')
    x = float(input('Digite o número: '))
    y = float(input('Digite o número: '))
    nome_da_operacao= input("Digite a função: ")
    

