def soma(a, b):
    return a + b

def divisao(a, b):  
    try:
        return a / b     
    except ZeroDivisionError:
        print('O divisão resulta em 0')
    
    