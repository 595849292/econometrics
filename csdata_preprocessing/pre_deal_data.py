import pandas as pd
import matplotlib.pylab as plt
import matplotlib

#============================
# applying fun[i] to column[i]
# param:
# column=['column_name1','column_name2',...]
# column_fun=[catfun1,catfun2,..]
#============================
def catfun1():
    pass
def catfun2():
    pass
def catogory_to_value(data,column,column_fun):
    # apply ith column element with fun to replace ith column
    data[column[i]] = list(map(data[column[i]], column_fun[i]))

def nullvalue():
    pass
def outer():
    pass

def transformation(replace_column_fun=None,withoutreplace_colunmn_fun=None):
    data=read_data('trend.xls')
    #data=get_data(data,column=['中国','美国'])
    #print(data)
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    a=data['测试1'].value_counts()
    a.plot(kind='bar')
    print(a)
    plt.show()
    print(a)
    print(type(a))

    '''
    data=data.drop(['美国','中国'],axis=1)
    print(data)
    data['额外']=[1]*data.shape[0]

    if replace_column_fun!=None:
        for i in range(len(replace_column_fun)):
            #apply ith column element with fun to replace ith column
            data[replace_column_fun[i][0]] = list(map(data[replace_column_fun[i][0]],replace_column_fun[i][1]))
    '''



if __name__ == '__main__':
    transformation()