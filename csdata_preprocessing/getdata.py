import pandas as pd
class Getdata():
    def __init__(self):
        pass

    # ============================
    # get data and rename their column name by dict
    # return dataframe
    # ============================
    def read_data(self,filename, sheetname='trend', newcolumnname=None):  # {'方法':'method','中国':'china'}
        data = pd.read_excel(filename, sheet_name=sheetname)

        if newcolumnname != None:
            if isinstance(newcolumnname, dict):
                data.rename(columns=newcolumnname, inplace=True)
            else:
                raise Exception('newcolumn_name is not dict')

        return data

    # ============================
    # params:
    # data type: dataframe
    # columns=['中国','美国',...] or [1:4]
    # row same as colums
    # ============================
    def getsub_data(self,data, column=None, row=None):
        if column != None:
            if isinstance(column[0], int):
                data = data.ix[:, column[0]:column[1]]
            else:
                data = data[column]
        if row != None:
            if isinstance(row[0], int):
                data = data.ix[row[0]:row[1], :]
            else:
                data = data[[row],]
        return data