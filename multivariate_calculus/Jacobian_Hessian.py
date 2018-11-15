# coding=utf-8
#https://docs.sympy.org/latest/tutorial/index.html

#===================================
# calculs Jacoobian and Hessian matrix
#===================================
import sympy
def fun1(x):
    J[x[0],x[1]]=x[2]
def fun2(x1):
    H[x1[0],x1[1]]=x1[2]

def JH(f,variant,Jaccobian=True,Hessian=True,determiant=True):
    if Jaccobian:
        jacobian = list(map(fun1, [[i, j, sympy.diff(fi, s)] for i, fi in enumerate(f) for j, s in enumerate(variant)]))
    if Hessian:
        hessian = list(map(fun2, [[i, j, sympy.diff(f_jac, v)] for i, f_jac in enumerate(J) for j, v in enumerate(variant)]))
    if determiant and Hessian:
        det=sympy.Matrix.det(H)
        print('=======det======')
        print(det)
        print('===============')

if __name__ == '__main__':
    #========param==================
    variant = sympy.symbols('x y z')
    f = sympy.sympify(['z*y*x**2'])
    #===============================
    J = sympy.zeros(len(f), len(variant))
    H = sympy.zeros(len(variant), len(variant))
    JH(f,variant)
    print(type(H))




