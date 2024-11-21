with open('Desafio Extra Palavras M e A\desafioListaDePalavras.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        palavra = linha.strip()
        if palavra.startswith('M') and palavra.endswith('a'):
            print(palavra)

