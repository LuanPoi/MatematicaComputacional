# -*- coding: utf-8 -*-
import numpy as np

class Bisseccao:
    def __init__(self, x, y, precisao):
        self.bisseccao(x, y, precisao)

    def f(self, x):
        return ((np.power((x + 1) , 2) * np.exp(np.power(x, 2) - 2)) - 1)

    def printResultado(self, resultado, precisao):
        print("-- Resultado --")
        if (resultado == None):
            print("Raiz: Não Existe")
        else:
            print("Raiz: " + str(resultado))
            print("Precisão: " + str(precisao))

    def bisseccao(self, x, y, precisao):
        iteracoes = 0
        while True:
            k = (x + y)/2

            if self.f(x) * self.f(k) == 0:
                self.printResultado(k, "Inf")
                break
            elif self.f(x) * self.f(k) < 0:
                y = k
            else:
                x = k

            j = (x + y)/2
            if  abs(j-k)/abs(j) < precisao:
                self.printResultado(k, precisao)
                break
            
            iteracoes = iteracoes + 1
            if (iteracoes >= 1000):
                self.printResultado(None, None)
                break

if __name__ == "__main__":
    print("--- MÉTODO DA BISSECÇÃO ---")
    
    x = float(input("Digite o valor de X:"))
    y = float(input("Digite o valor de y:"))
    precisao = float(input("Digite a precisao:"))
    
    Bisseccao(x, y, precisao)