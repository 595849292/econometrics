#=========================
# first fillna with NULL
# use observation fun to look at data
# use plot fun to fun and replace null and others
#=========================
import matplotlib.pylab as plt
class Null_discrete():
    def __init__(self):
        self.data=None
        #pass
    #====================
    # pseries is pandas Series
    # rule is dict {'中国'：1，'美国'：2}
    #====================
    def substitution(self,pseriess=None,rule=None):
        ps= pseriess.map(rule)
        return ps

    def observation(self,data=None):
        data[data.isna()] = 'NULL'
        res=[data.ix[:,i].value_counts() for i in range(0,data.shape[1])]
        [print(each) for each in res]

    def plot_figure(self,data):
        #data = pd.read_excel('trend.xls', sheet_name='trend')[['测试1', '测试2']]
        data[data.isna()] = 'NULL'
        rulelist=[]
        #rulelist=[{'中国':1,'苏联':2},{'清华':1,'北大':2,'青大':3}]
        column_name=[]
        #column_name=['测试1', '测试2']
        for i in range(0,len(column_name)):
            data[column_name[i]]=self.substitution(data[column_name[i]],rulelist[i])
            num=data[column_name[i]].value_counts()
            plt.subplot(len(column_name),1,i+1)
            num.plot(kind='bar')
        plt.show()
        return data



if __name__ == '__main__':
    a=Null_discrete()
    a.plot_figure()