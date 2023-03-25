import lib_04 as l
import math
import numpy as np
import Matrices as c
def E1_E2 ():
    print("#4.3.1")
    v1 = np.array([(1, 0), (0, 0)])
    observable_x = np.array([[(0, 0), (1, 0)], [(1, 0), (0, 0)]])
    vr = c.accion(observable_x, v1)
    valores_x, vectores_x = np.linalg.eig(observable_x)
    print("El resultado de la observacion es: ", vr)
    print("Los valores propios del observable son: ", valores_x, "ademas sus vectores propios son: "
          , vectores_x," por tanto el sistema colapsa en un vector propio")
    j = []
    a = vectores_x.tolist()
    for i in range(len(a)):
        for x in range(len(a[0])):
            j.append(a[i][x])
    print("4.3.2")
    for i in range(1,len(j)):
        print("la pobabilidad de que el sistema colapse en el vector",j[i],"es:",c.norma((c.interno(v1,j[i]) / c.norma(j[i])).tolist()))
def E3():
    m1 = [[0,1],[1,0]]
    m2 = [[math.sqrt(2)/2,math.sqrt(2)/2],[math.sqrt(2)/2,-math.sqrt(2)/2]]
    a = c.prod_matr(c.adj_matr(m2),m2)
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = round(a[i][j])
    if c.unitaria(m1) and c.unitaria(a):
        if c.unitaria(c.prod_matr(m1,a)):
            print("#4.4.1")
            print(True)
def E4():
    print("4.4.2")
    a = l.dynamic(np.array([[0, 1 / math.sqrt(2), 1 / math.sqrt(2), 0],
                            [1j / math.sqrt(2), 0, 0, 1 / math.sqrt(2)],
                            [1 / math.sqrt(2), 0, 0, 1j / math.sqrt(2)],
                            [0, 1 / math.sqrt(2), -1 / math.sqrt(2), 0]]),
                            [1, 0, 0, 0], 3)
    print(a.tolist())
def main():
    E1_E2()
    E3()
    E4()
main()


