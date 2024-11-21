with open('desafioFinalPalavras.txt', 'r', encoding='utf-8') as a:
    with open('comecaB_terminaO.txt', 'w', encoding='utf-8') as r:
        for linha in a:
            palavra = linha.strip()
            if palavra.startswith('B') and palavra.endswith('o'):
                r.write(palavra +'\n')