import numpy as np
def check_definite(mat):
    ma=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    result=[np.linalg.det(ma[0:i,0:i]) for i in range(1,len(ma)+1)]
    if len(([True for each in result if each>0]))==len(ma):
        print('Matrix is positive definite')
    elif len([True for each in result if each>=0])==len(ma):
        print('Matrix is positive semidefinite')
    elif len([True for i in range(0,len(result)) if result[i]*(-1)**(i)>0])==len(ma):
        print('Matrix is negative definite')
    elif len([True for i in range(0,len(result)) if result[i]*(-1)**(i)>=0])==len(ma):
        print('Matrix is negative semidefinite')
    else:
        print('Matrix is indefinite')
    print(all([-1,2,3]))