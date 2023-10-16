from pc import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f'Processando {titulo}')
    for i in lista:
        print(i, '==>', funcao(i))

processar('Dobros de 1 a 10', range(1,11), dobro) 
processar('Quadrados de 1 a 10', range(1,11), quadrado)