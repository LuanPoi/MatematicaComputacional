import numpy as np

def f(x):
    return ((np.power((x + 1) , 2) * np.exp(np.power(x, 2) - 2)) - 1)

def printResultado(resultado, precisao):
    print("-- Resultado --")
    if (resultado == None):
        print("Raiz: Não Existe")
    else:
        print("Raiz: " + str(resultado))
        print("Precisão: " + str(precisao))

def bisseccao(x, y, precisao):
    iteracoes = 0
    while True:
        k = (x + y)/2

        if f(x) * f(k) == 0:
            printResultado(k, "Inf")
            break
        elif f(x) * f(k) < 0:
            y = k
        else:
            x = k

        j = (x + y)/2
        if  abs(j-k)/abs(j) < precisao:
            printResultado(k, precisao)
            break
        
        iteracoes = iteracoes + 1
        if (iteracoes >= 1000):
            printResultado(None, None)
            break

if __name__ == "__main__":
    print("--- MÉTODO DA BISSECÇÃO ---")
    
    x = float(input("Digite o valor de X:"))
    y = float(input("Digite o valor de y:"))
    precisao = float(input("Digite a precisao:"))
    
    bisseccao(x, y, precisao)