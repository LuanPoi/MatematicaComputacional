# -*- coding: utf-8 -*-
import numpy as np

class Secantes:
    def __init__(self, x, y, precisao):
        self.secantes(x, y, precisao)

    def f(self, x):
        return ((np.power((x + 1) , 2) * np.exp(np.power(x, 2) - 2)) - 1)

    def printResultado(self, resultado, precisao):
        print("-- Resultado --")
        if (resultado == None):
            print('Deu zero na derivada.')
        else:
            print("Raiz: " + str(resultado))
            print("Precisão: " + str(precisao))

    def secantes(self, y, x, precisao):
        valores = []
        valores.append({ "X":y, "fX":self.f(y) })
        
        while True:
            f = self.f(x)
            valores.append({ "X":x, "fX":f })
            if(valores[len(valores) - 1]["fX"] == 0):
                self.printResultado(x, 0)
                return
            fKmais1 = ((valores[len(valores) - 2]["X"]) * (valores[len(valores) - 1]["fX"]) - (valores[len(valores) - 1]["X"]) * (valores[len(valores) - 2]["fX"])) / ((valores[len(valores) - 1]["fX"]) - (valores[len(valores) - 2]["fX"]))
            
            erroRelativo = abs(fKmais1 - x) / abs(fKmais1)
            if erroRelativo < precisao:
                self.printResultado(x, erroRelativo)
                return
            x = fKmais1
            
            if (len(valores) >= 1000):
                self.printResultado(None, None)
                break

if __name__ == "__main__":
    print("--- MÉTODO DE SECANTES ---")
    
    x = float(input("Digite o valor de X:"))
    y = float(input("Digite o valor de Y:"))
    precisao = float(input("Digite a precisao:"))
    
    Secantes(x, y, precisao)