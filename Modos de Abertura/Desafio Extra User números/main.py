def divisao(a, b):
    return a /b


print('Digite dois números para dividirmos!')
for numero in range(10):
    n1 = float(input(f'{numero + 1} - Digite um número: '))
    n2 = float(input(f'{numero + 1} - Digite outro número: '))
    print('-' * 30)
    try:
        with open('Desafio Extra User números/divisão.txt','a') as arquivo:
            arquivo.write((str(divisao(n1, n2)) + '\n'))
    except ValueError:
        print('Erro!')