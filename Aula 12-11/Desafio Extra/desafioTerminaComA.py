with open('desafioListaDePalavras.txt', 'r', encoding='utf-8') as arquivo:
    with open('terminaA.txt', 'w', encoding='utf-8') as file:
        for linha in arquivo:
            palavra = linha.strip()
            if palavra.endswith('a'):
                file.write(palavra +'\n')