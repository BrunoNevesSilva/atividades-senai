#from modulo.operacoes import soma
from modulo.verificacao import verificar_par
from modulo.multiplicar import multiplicar
from modulo.subtrair import subtrair

#print(f'A soma de 5 com 5 é :',soma(5, 5))

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

verificar_par(n1)
verificar_par(n2)
print(subtrair(n1, n2))
print(multiplicar(n1, n2))