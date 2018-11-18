#=================================
# add/delete some row/columns
#=================================

class Add_Drop():
    def __init__(self):
        pass

    # ============================
    # param:
    # above_num/below_num: insert data between above_num and below_num
    # insertRow: insert row(type:dataframe )
    # ex:  insertRow = pd.DataFrame([[0, 1]], columns=['中国', '美国'])
    # ============================
    def row_add(self,data, above_num, below_num, insertRow):
        above = data.loc[:above_num]
        below = data.loc[below_num:]
        newdata = above.append(insertRow, ignore_index=True).append(below, ignore_index=True)
        return newdata

    # ============================
    # param:
    # rowindex=[0,1,3,4]
    # ============================
    def row_drop(self,data, rowindex):
        data = data.drop(rowindex)
        return data

    # ============================
    # param:
    # column_name=['column_name1','column_name2',...]
    # insertColumn=[[1,2,.],[3,4,..],...]
    # ============================
    def column_add(self,data, colum_name, insertColumn):
        for i in range(0, len(colum_name)):
            data[colum_name[i]] = insertColumn[i]
        return data

    # ============================
    # param:
    # column_name=['column_name1','column_name2',...]
    # insertColumn=[[1,2,.],[3,4,..],...]
    # ============================
    def column_drop(self,data, colum_name):
        for i in range(0, len(colum_name)):
            data = data.drop(colum_name)
        return data
