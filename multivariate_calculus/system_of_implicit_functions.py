# coding=utf-8
import sympy
import random

#======================
# derive the derivative in terms of system of implicit functions
# __init__  define initial parameters
#======================
class Implicit_Fun():
    def __init__(self):
        self.variant = sympy.symbols('x y a')
        self.variant_value=[0,1,2]
        self.F = sympy.simplify(['x**2+a*x*y+y**2-1', 'x**2+y**2-a**2+3'])
        #self.x=0
        #self.y = 1
        #self.a = 2

        self.J = sympy.zeros(len(self.F), len(self.variant))
    def fun1(self,x):
        self.J[x[0], x[1]]=x[2]

    def fun2(self,x1):
        self.op_va.remove(x1)
    def fun3(self,x):
        self.temp1[x[0], x[1]] = x[2]
    def cal_funvalue(self,x1):
        for i in range(0,len(self.variant)):
            if i==0:
                f = x1.subs(self.variant[i], self.variant_value[i])
            else:
                f=f.subs(self.variant[i], self.variant_value[i])
        #x=self.x
        #y=self.y
        #a=self.a
        #f=eval(str(x1))
        return f

    def cal_Jacoobian(self,variant_str):
        list(map(self.fun3, [[i, j, sympy.diff(fi, v)] for j, v in enumerate(sympy.symbols(variant_str)) for i, fi in
                        enumerate(self.F)]))
        det1 = sympy.Matrix.det(self.temp1)
        det2 = self.cal_funvalue(det1)
        return det1,det2

    def cal_dydx(self,y, x):  # dy/dx
        #free_variable_num = len(self.variant) - len(self.F)
        self.op_va = [str(each) for each in self.variant]
        list(map(self.fun2,[y,x]))
        while True:
            index = random.sample(range(0, len(self.op_va)), len(self.F) - 1)
            variant1 = [self.op_va[i] for i in index]
            variant1.append(y)
            #variant2 = [self.op_va[i] for i in list(set(range(0, len(self.op_va))) - set(index))]
            #variant2.append(x)
            # check if we can solve for variant1 as a function of variant2
            self.temp1=sympy.zeros(len(self.F),len(variant1))
            variant1_str=' '.join(variant1)
            det1,det_value1=self.cal_Jacoobian(variant1_str)

            if det_value1>0:
                print(variant1_str+' can be as a function of other variables')
                print('det1:'+str(det1))
                break
        variant2_str=variant1_str.replace(y,x)
        det2,det_value2=self.cal_Jacoobian(variant2_str)
        print('det2:'+str(det2))
        det=-det_value2/det_value1
        print('det:'+str(det))




if __name__ == '__main__':
    a=Implicit_Fun()
    a.cal_dydx('y','a')
    #b=a.cal_funvalue('x+y+a')
    #print(b)
    '''
    
    cal_Jacoobian()
    #print(J)
    w=sympy.Matrix([[J[0,0],J[0,1]],[J[1,0],J[1,1]]])
    det=sympy.Matrix.det(w)
    #print(det)
    cal_dydx('y','x')
    '''