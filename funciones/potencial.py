import sympy as sp
import numpy as np
import math as mt    #calculos matematicos y constantes


#parametros del potencial V
C, V_0, x_0 = -1.1, 1/(2*mt.pi), -0.19

#estableciendo el potencial V
X =sp.symbols('X')
expr1 = V_0*(sp.sin(2*sp.pi*(X-x_0)) +1/4 *sp.sin(4*sp.pi*(X-x_0))) #potencial V
expr2=sp.diff(expr1,X)   

#haciendo que V tome como argumentos vectores
V =sp.lambdify(X, expr1)
V_vector =np.vectorize(V)
Vdiff = sp.lambdify(X,expr2)
Vdiff_vector =np.vectorize(Vdiff)

#estableciendo el potencial efectivo U=V-F*x
def U(x,a,F,fact):  # a=0: V=0, a=1: V   ,fact:cambiar el periodo
    return a*V_vector(x*fact)-F*x
U_vector = np.vectorize(U)
#fuerza correspondiente de U
def FU(x,a,F,fact):   
    if a==0:
        return F
    return -a*Vdiff_vector(x*fact)+F
FU_vector = np.vectorize(FU,excluded=['a','F'])