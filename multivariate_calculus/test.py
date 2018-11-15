import sympy
'''
w='-2*a*x**2 + 2*a*y**2'
f=sympy.simplify(w)

variant=sympy.symbols('x y a')

a1=sympy.diff(f,variant[0])
a2=sympy.diff(f,variant[1])
a3=[1,2,3]
for i in range(3):
    if i==0:
        f=a1.subs(variant[i],a3[i])
    else:
        f=f.subs(variant[i],a3[i])
print(f)
'''

a1=sympy.symbols('a1')
a2=sympy.symbols('a2')
a3=sympy.symbols('a3')
a4=sympy.symbols('a4')
a5=sympy.symbols('a5')
a6=sympy.symbols('a6')
a7=sympy.symbols('a7')
a8=sympy.symbols('a8')
a9=sympy.symbols('a9')
a10=sympy.symbols('a10')

b0=sympy.symbols('b0')
b1=sympy.symbols('b1')
b2=sympy.symbols('b2')
b3=sympy.symbols('b3')

y1=sympy.symbols('y1')
y2=sympy.symbols('y2')
y3=sympy.symbols('y3')
y4=sympy.symbols('y4')

b=sympy.solve([a1*b0+a2*b1+a3*b2+a4*b3-y1,a2*b0+a5*b1+a6*b2+a7*b3-y2,a3*b0+a6*b1+a8*b2+a9*b3-y3,a4*b0+a8*b1+a9*b2+a10*b3-y4],[b0,b1,b2,b3])
print(b)



{b0: (-y1*(a10*a5*a8 - a10*a6**2 - a5*a9**2 + a6*a7*a9 + a6*a8*a9 - a7*a8**2) + y2*(a10*a2*a8 - a10*a3*a6 - a2*a9**2 + a3*a8*a9 + a4*a6*a9 - a4*a8**2) - y3*(a10*a2*a6 - a10*a3*a5 - a2*a7*a9 + a3*a7*a8 + a4*a5*a9 - a4*a6*a8) + y4*(a2*a6*a9 - a2*a7*a8 - a3*a5*a9 + a3*a6*a7 + a4*a5*a8 - a4*a6**2))/(-a1*a10*a5*a8 + a1*a10*a6**2 + a1*a5*a9**2 - a1*a6*a7*a9 - a1*a6*a8*a9 + a1*a7*a8**2 + a10*a2**2*a8 - 2*a10*a2*a3*a6 + a10*a3**2*a5 - a2**2*a9**2 + a2*a3*a7*a9 + a2*a3*a8*a9 + 2*a2*a4*a6*a9 - a2*a4*a7*a8 - a2*a4*a8**2 - a3**2*a7*a8 - 2*a3*a4*a5*a9 + a3*a4*a6*a7 + a3*a4*a6*a8 + a4**2*a5*a8 - a4**2*a6**2),
 #b1: (y1*(a10*a2*a8 - a10*a3*a6 - a2*a9**2 + a3*a7*a9 + a4*a6*a9 - a4*a7*a8) + y2*(-a1*a10*a8 + a1*a9**2 + a10*a3**2 - 2*a3*a4*a9 + a4**2*a8) + y3*(a1*a10*a6 - a1*a7*a9 - a10*a2*a3 + a2*a4*a9 + a3*a4*a7 - a4**2*a6) - y4*(a1*a6*a9 - a1*a7*a8 - a2*a3*a9 + a2*a4*a8 + a3**2*a7 - a3*a4*a6))/(-a1*a10*a5*a8 + a1*a10*a6**2 + a1*a5*a9**2 - a1*a6*a7*a9 - a1*a6*a8*a9 + a1*a7*a8**2 + a10*a2**2*a8 - 2*a10*a2*a3*a6 + a10*a3**2*a5 - a2**2*a9**2 + a2*a3*a7*a9 + a2*a3*a8*a9 + 2*a2*a4*a6*a9 - a2*a4*a7*a8 - a2*a4*a8**2 - a3**2*a7*a8 - 2*a3*a4*a5*a9 + a3*a4*a6*a7 + a3*a4*a6*a8 + a4**2*a5*a8 - a4**2*a6**2),
 b2: (-y1*(a10*a2*a6 - a10*a3*a5 - a2*a8*a9 + a3*a7*a8 + a4*a5*a9 - a4*a6*a7) + y2*(a1*a10*a6 - a1*a8*a9 - a10*a2*a3 + a2*a4*a9 + a3*a4*a8 - a4**2*a6) - y3*(a1*a10*a5 - a1*a7*a8 - a10*a2**2 + a2*a4*a7 + a2*a4*a8 - a4**2*a5) + y4*(a1*a5*a9 - a1*a6*a7 - a2**2*a9 + a2*a3*a7 + a2*a4*a6 - a3*a4*a5))/(-a1*a10*a5*a8 + a1*a10*a6**2 + a1*a5*a9**2 - a1*a6*a7*a9 - a1*a6*a8*a9 + a1*a7*a8**2 + a10*a2**2*a8 - 2*a10*a2*a3*a6 + a10*a3**2*a5 - a2**2*a9**2 + a2*a3*a7*a9 + a2*a3*a8*a9 + 2*a2*a4*a6*a9 - a2*a4*a7*a8 - a2*a4*a8**2 - a3**2*a7*a8 - 2*a3*a4*a5*a9 + a3*a4*a6*a7 + a3*a4*a6*a8 + a4**2*a5*a8 - a4**2*a6**2),
 b3: (y1*(a2*a6*a9 - a2*a8**2 - a3*a5*a9 + a3*a6*a8 + a4*a5*a8 - a4*a6**2) - y2*(a1*a6*a9 - a1*a8**2 - a2*a3*a9 + a2*a4*a8 + a3**2*a8 - a3*a4*a6) + y3*(a1*a5*a9 - a1*a6*a8 - a2**2*a9 + a2*a3*a8 + a2*a4*a6 - a3*a4*a5) + y4*(-a1*a5*a8 + a1*a6**2 + a2**2*a8 - 2*a2*a3*a6 + a3**2*a5))/(-a1*a10*a5*a8 + a1*a10*a6**2 + a1*a5*a9**2 - a1*a6*a7*a9 - a1*a6*a8*a9 + a1*a7*a8**2 + a10*a2**2*a8 - 2*a10*a2*a3*a6 + a10*a3**2*a5 - a2**2*a9**2 + a2*a3*a7*a9 + a2*a3*a8*a9 + 2*a2*a4*a6*a9 - a2*a4*a7*a8 - a2*a4*a8**2 - a3**2*a7*a8 - 2*a3*a4*a5*a9 + a3*a4*a6*a7 + a3*a4*a6*a8 + a4**2*a5*a8 - a4**2*a6**2)}



#(y1*(a10*a2*a8 - a10*a3*a6 - a2*a9**2 + a3*a7*a9 + a4*a6*a9 - a4*a7*a8) + y2*(-a1*a10*a8 + a1*a9**2 + a10*a3**2 - 2*a3*a4*a9 + a4**2*a8) + y3*(a1*a10*a6 - a1*a7*a9 - a10*a2*a3 + a2*a4*a9 + a3*a4*a7 - a4**2*a6) - y4*(a1*a6*a9 - a1*a7*a8 - a2*a3*a9 + a2*a4*a8 + a3**2*a7 - a3*a4*a6))


#(-a1*a10*a5*a8 + a1*a10*a6**2 + a1*a5*a9**2 - a1*a6*a7*a9 - a1*a6*a8*a9 + a1*a7*a8**2 + a10*a2**2*a8 - 2*a10*a2*a3*a6 + a10*a3**2*a5 - a2**2*a9**2 + a2*a3*a7*a9 + a2*a3*a8*a9 + 2*a2*a4*a6*a9 - a2*a4*a7*a8 - a2*a4*a8**2 - a3**2*a7*a8 - 2*a3*a4*a5*a9 + a3*a4*a6*a7 + a3*a4*a6*a8 + a4**2*a5*a8 - a4**2*a6**2)