'''
cvxpy的prob.status可以有如下状态值： 
OPTIMAL: 问题被成功解决 
INFEASIBLE：问题无解 
UNBOUNDED：无边界 
OPTIMAL_INACCURATE：解不精确 
INFEASIBLE_INACCURATE： 
UNBOUNDED_INACCURATE： 
'''
#http://www.cvxpy.org/tutorial/index.html

from cvxpy import *
x=Variable()
y=Variable()
constraints=[x+y==1,x-y>=1]
obj=Minimize(square(x-y))
prob=Problem(obj,constraints)
prob.solve()

print(prob.status)
print(prob.value)
print(x.value)
