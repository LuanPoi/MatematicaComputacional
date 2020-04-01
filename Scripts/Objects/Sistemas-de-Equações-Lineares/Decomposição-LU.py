# -*- coding: utf-8 -*-
import numpy as np

class DecomposicaoLU:
    def __init__(self):
        self.LU()

    def LU(self):
        A = [[5,2,1],[3,1,4],[1,1,3]]
        b = [0, -7, -5]
        n = len(A)

        for i in range(i, n):
            for j in range(n):
                if i <= j:
                    soma = 0
                    for k in range(i):
                        soma = soma + A[i][k] * A[k][j]
                    A[i][k] = A[i][j] - soma
                elif i > j:
                    soma = 0
                    for k in range(j):
                        soma = soma + A[i][k] * A[k][j]
                    A[i][j] = (A[i][j] - soma) / A[j][j]
        print("\nNa parte estritamente inferior da matriz estão...")
        print(A)

        #Resolução de Ly=b
        for i in range(1,n):
            soma = 0
            for j in range(i):
                soma = soma + A[i][j] * b[j]
            b[i] = b[i] - soma
        print("\n Solução de Ly=b, y =", b)

        #Resolução de Ux=y
        b[n-1] = b[n-1] / A[n-1][n-1]
        for h in range(n-2, -1, -1):
            soma = 0
            for j in range(h+1, n):
                soma = soma + A[h][j] * b[j]
            b[h] = (b[h] - soma) / A[h][h]
        print("\nSolução de Ux=y, x =", b)

if __name__ == "__main__":
    print("--- MÉTODO DA DECOMPOSIÇÂO LU ---")
    DecomposicaoLU()