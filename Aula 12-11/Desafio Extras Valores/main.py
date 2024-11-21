from modulo.divisao import divisao

resultado = []
def retorneResultadosDivisao(arquivo):
    with open('valores.txt', 'r') as arquivo:
        for linha in arquivo:
            try:
                numero = float(linha.strip()) 
                resultado = divisao(numero)  
                resultados.append(resultado)
            except ValueError:
                print('Erro')
    return resultados

resultados = retorneResultadosDivisao('valores.txt')
print(resultados)