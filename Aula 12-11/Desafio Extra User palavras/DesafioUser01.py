for palavra in range(10):
    palavras = str(input(f'Digite a {palavra + 1 }ª palavra: ').capitalize())
    if palavras.startswith('A'):
        with open('palavras_a.txt','a')as arquivo:
            arquivo.write(palavras +'\n')
    else:
        with open('demais_palavras.txt', 'a') as file:
            file.write(palavras + '\n')
    
