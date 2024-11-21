#Aqui estamos importa a operação de soma na pasta aritmetica.
from aritmetica.operacoes import *

#Aqui estamos importa a operação de soma na pasta geometria.
from geometria.formas import areaRetangulo


def main():
    print('Digite dois números para fazermos a soma')
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    print(f'A soma de {a} e {b} é :{soma(a, b)}') 

    #Aqui estamos testando para verificar se a divisaõ resulta em 0.
    divisao(a, b)

    print('------------------------------------------------------')
    
    print('Descobrir a área do retângulo')
    altura = float(input('Digite a altura: '))
    largura = float(input('Digite a largura: '))
    print(f'A área desse retângulo é: {areaRetangulo(largura, altura)}')

if __name__ == '__main__':
    main()