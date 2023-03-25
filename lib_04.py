import numpy as np
import math
import Matrices as c

#4.1
#1
def prob_pos(v,x):
     a = (v[x].real)**2 + (v[x].imag)**2
     return c.norma(v)**2 / a
#2
def amp(v1,v2):
    return c.interno(v1,v2) / (c.norma(v1)*c.norma(v2))
#1
def obs(o,v1,v2):
    probabilidad = np.abs(np.dot(v1, np.dot(o, v2))) ** 2
    return probabilidad
#2
def med_var(m,v):
    if c.hermitiana(m):
        media = np.dot(v.conj(), np.dot(m, v))
        varianza = np.dot(v.conj(), np.dot(m ** 2, psi)) - media ** 2
        return media,varianza
# 3
def prob_vec(x0, obs, pos):
    vectores = valores_vectores(obs)[1]
    return amp(x0, vectores[pos])
# 4
def dynamic(mat,vec,t):
    if c.unit_comp(mat):
        for i in range(t):
            vec = c.accion(mat, vec)
        return vec
    else:
        return "la matriz no es unitaria"

