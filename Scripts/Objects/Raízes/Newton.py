# -*- coding: utf-8 -*-
import numpy as np

class Newton:
    def __init__(self, x, precisao):
        self.newton(x, precisao)

    def f(self, x):
        return ((np.power((x + 1) , 2) * np.exp(np.power(x, 2) - 2)) - 1)

    def fLinha(self, x):
        return (2 * np.exp(-2 + np.power(x, 2)) * (1 + 2 * x + 2 * np.power(x, 2) + np.power(x, 3)))

    def printResultado(self, resultado, precisao):
        print("-- Resultado --")
        if (resultado == None):
            print('Deu zero na derivada.')
        else:
            print("Raiz: " + str(resultado))
            print("Precisão: " + str(precisao))

    def newton(self, x, precisao):
        valores = []
        while True:
            f = self.f(x)
            fLinha = self.fLinha(x)
            valores.append({ "X":x, "fX":f, "fLinhaX":fLinha })
            debug = valores[len(valores) - 1]
            if(valores[len(valores) - 1]["fX"] == 0):
                self.printResultado(x, 0)
                return
            if(valores[len(valores) - 1]["fLinhaX"] == 0):
                self.printResultado(None, None)
                return
            fKmais1 = x  - ((valores[len(valores) - 1]["fX"])/(valores[len(valores) - 1]["fLinhaX"]))
            erroRelativo = abs(fKmais1 - x) / abs(fKmais1)
            if erroRelativo < precisao:
                self.printResultado(x, erroRelativo)
                return
            x = fKmais1
            
            if (len(valores) >= 1000):
                self.printResultado(None, None)
                break

if __name__ == "__main__":
    print("--- MÉTODO DE NEWTON ---")
    
    x = float(input("Digite o valor de X:"))
    precisao = float(input("Digite a precisao:"))
    
    Newton(x, precisao)