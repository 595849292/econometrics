import pandas as pd
def read_data_ts():
    pass
def get_data_ts():
    pass

def read_data(filename,sheetname='trend',newcolumnname=None): #{'方法':'method','中国':'china'}
    data=pd.read_excel(filename,sheet_name=sheetname)

    if newcolumnname!=None:
        if isinstance(newcolumnname,dict):
            data.rename(columns=newcolumnname,inplace=True)
        else:
            raise Exception('newcolumn_name is not dict')

    return data
#params:
# data type: dataframe
# columns=['中国','美国',...] or [1:4]
# row same as colums
def get_data(data,column=None,row=None):
    if column!=None:
        if isinstance(column[0],int):
            data=data.ix[:,column[0]:column[1]]
        else:
            data=data[column]
    if row!=None:
        if isinstance(row[0],int):
            data=data.ix[row[0]:row[1],:]
        else:
            data=data[[row],]
    return data

def catogory_to_value():
    pass
def nullvalue():
    pass
def outer():
    pass

def transformation(replace_column_fun=None,withoutreplace_colunmn_fun=None):
    data=read_data('trend.xls')
    data=get_data(data,column=['中国','美国'])
    print(data)
    data=data.drop(['美国'],axis=1)
    print(data)


    if replace_column_fun!=None:
        for i in range(len(replace_column_fun)):
            #apply ith column element with fun to replace ith column
            data[replace_column_fun[i][0]] = list(map(data[replace_column_fun[i][0]],replace_column_fun[i][1]))




if __name__ == '__main__':
    transformation()