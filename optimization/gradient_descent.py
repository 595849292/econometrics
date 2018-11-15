# it solve for unconstrained optimization problem
# example   f=x**2+Y**2
import time
import numpy as np
import sympy
class GD():
    def __init__(self):
        self.variant='x y z'
        self.inivalue=[1,2,3]
        self.fvalue=0
        self.f=sympy.simplify('x**2+y**3+z')

    def fun1(self,x):
        variant=self.variant.split(' ')
        for i in range(0,len(x)):
            if i==0:
                self.fvalue=self.f.subs(variant[i],self.inivalue[i])
            else:
                self.fvalue=self.fvalue.sub(variant[i],self.inivalue[i])

        return self.fvalue
    def gradient(self,f):
        fvalue=''
        variant = self.variant.split(' ')
        for i in range(0, len(f)):
            if i == 0:
                fvalue = f.subs(variant[i], self.inivalue[i])
            else:
                fvalue = fvalue.sub(variant[i], self.inivalue[i])

        return fvalue

    def gradient_descent(self):
        variant=sympy.symbols(self.variant)
        f=sympy.simplify(self.f)
        #variant=self.variant.split(' ')
        diff=[sympy.diff(f,variant[i])for i in range(0,len(variant))]
        second_error=1000
        second_y=self.fun1(self.inivalue)
        while True:
            direction=[self.gradient(f) for f in diff]
            self.inivalue=np.array(self.inivalue)-np.array(direction)
            first_error=second_error

            first_y=second_y
            second_y=self.fun1(self.inivalue)

            second_error=abs(second_y-first_y)

            if second_error>first_error or second_error<0.01:
                print(self.inivalue)
                print(second_error)
                print(first_error)
                break






