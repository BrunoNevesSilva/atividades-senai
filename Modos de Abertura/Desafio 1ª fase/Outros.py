'''
frase = input('Digite uma frase: ').capitalize()

def verificar_inicio(): 
    if frase.startswith("Olá"):
        print('Inicia com Olá')
    else:
        print('Não inicia')

verificar_inicio()


frase = input('Digite sua frase: ')

def escrever(x):
    with open('arquivo.txt','w') as arquivo:
        arquivo.write(frase)

escrever(frase)

n1 = 0
with open('numeros.txt','r') as arquivo:
    for numero in arquivo:
        numero = int(arquivo)
        if numero % 3 == 0:
            n1 = int(numero) + n1
    

print(n1)
'''
soma = 0

with open('numeros.txt','r') as arquivo:
    try:   
        for linha in arquivo:
            numero = float(linha)
            if numero % 3 == 0:
                soma += numero
    except ValueError:
        print('Valor Invalido!')
print(soma)
'''

with open('texto.txt','r') as arquivo:
    for linha in arquivo:
        comB = linha.startswith('B')
        with open('comB.tx','w') as arquivo:
            arquivo.write(comB)
'''