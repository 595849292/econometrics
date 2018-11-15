# coding=utf-8
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARMA
from dateutil.relativedelta import relativedelta
import pickle
from sklearn.externals import joblib
#================================================================================================================
# 待优化部分：模型进行外延预测时，需要确认根据m区间数据，预测未来n 区间数值，从而动态更新模型，其中目标函数不能简单设定为准确率最大
# 该部分可以采用遗传算法进行最优参数的寻找，同时采用K折交叉验证进行验证
#================================================================================================================
#rng=pd.date_range('1/1/2011',periods=6,freq='H')
#ts=pd.Series(np.random.randn(len(rng)),index=rng)
#converted=ts.asfreq('3H')
#a=ts.resample('2H').sum().head(5)

class ARMA_TS():
    def __init__(self):
        pass
    def read_data(self,path,tscolu='TravelDate',datacol='Passengers'):
        df=pd.read_csv(path, encoding='utf-8',index_col=tscolu)
        df.index=pd.to_datetime(df.index)
        ts=df[datacol]
        return ts
    #============================================#
    # 分析部分，确定数据平稳，所需要的差分和移动平均操作#
    #============================================#

    #================================
    # 绘制原始时间序列的折线图
    #================================
    def draw_ts(self,ts):
        plt.figure(facecolor='white')
        ts.plot(color='black')
        plt.legend('time series')
        plt.show()
    # ================================
    # 绘制普通移动平均图和加权平均图，观察趋势
    # ================================
    def draw_trend(self,ts,size):
        plt.figure(facecolor='white')
        #对size个数据进行移动平均
        rol_mean=ts.rolling(window=size).mean()
        #对size个数据进行加权平均
        rol_weighted_mean=pd.ewma(ts,span=size)

        ts.plot(color='black',label='Original')
        rol_mean.plot(color='black',linestyle='dashed',label='Rolling Mean')
        rol_weighted_mean.plot(color='black',linestyle='dotted',label='Weighted Rolling Mean')

        plt.legend(loc='best')
        plt.title('Rolling Mean')
        plt.show()
    # ================================
    # 绘制时间序列的原始部分、趋势部分、季节部分和残差部分
    # ================================
    def decompose_transformation(self,ts):
        decomposition=seasonal_decompose(ts,model="additive")
        trend=decomposition.trend.dropna()
        seasonal=decomposition.seasonal.dropna()
        residual=decomposition.resid.dropna()
        plt.figure(facecolor='white')
        ax1=plt.subplot(411)
        ts.plot(color='black',linestyle='dashed',label='Original',ax=ax1)
        ax2=plt.subplot(412)
        trend.plot(color='black',linestyle='dashed',label='Trend',ax=ax2)
        ax3 = plt.subplot(413)
        seasonal.plot(color='black',linestyle='dashed',label='Seasonality',ax=ax3)
        ax4 = plt.subplot(414)
        residual.plot(color='black',linestyle='dashed',label='Residuals',ax=ax4)
        plt.show()

    # ================================
    # 采用ADF方法检验时间序列的平稳性,p<alfa 则序列平稳
    # ================================
    def test_Stationarity(self,ts):
        '''
        regression: str
        {'c', 'ct', 'ctt', 'nc'}
        *'c': constant only(default)
        *'ct': constant and trend
        *'ctt': constant, and linear and quadratic trend
        *'nc': no constant, no trend
        '''
        dftest=adfuller(ts,regression="ct")
        dfoutput = pd.Series(dftest[0:4],
                             index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput['Critical Value (%s)' % key] = value
        return dfoutput

    # ================================
    # 绘制自相关图和偏相关图，确定p和q值
    # ================================
    def draw_acf_pacf(self, ts, lags=31):
        plt.figure(facecolor='white')
        ax1 = plt.subplot(211)
        plot_acf(ts, lags=lags, ax=ax1)
        ax2 = plt.subplot(212)
        plot_pacf(ts, lags=lags, ax=ax2)
        plt.show()

    # ================================
    # 对时间序列进行ln变换
    # ================================
    def log_transformation(self,ts):
        return np.log(ts)

    # ================================
    # 对时间序列进行差分变换
    # ================================
    def diff_transformation(self,ts,lag):
        diff=ts.diff(lag)
        diff.dropna(inplace=True)
        return diff

    # ===============================
    # 进行移动平均和差分处理
    # ===============================
    def remove_season_diff(self,ts,rolling_size,diff_size):
        rolling_mean=ts.rolling(window=rolling_size).mean()
        rolling_mean.dropna(inplace=True)
        ts_diff=rolling_mean.diff(diff_size)
        return ts_diff
    # ===============================
    # 建立ARMA模型
    # ===============================
    def creatmodel(self,ts,p,q):
        model=ARMA(ts,order=(p,q))
        result_arma=model.fit(disp=-1,method='css',maxiter=50)

        return result_arma
    #===============================
    #评估模型样本内的误差，采用均方根误差(RMSE)
    #===============================
    def evaluate_error(self,log_recover,ts):
        ts=ts[log_recover.index]
        plt.figure(facecolor='white')
        log_recover.plot(color='black',label='Predict')
        ts.plot(color='black',linestyle='dashed',label='Original')
        plt.legend(loc='best')
        plt.title('RMSE: %.4f'% np.sqrt(sum((log_recover-ts)**2)/ts.size))
        plt.show()

    #==============================
    #对时间序列进行差分和移动平均 d=[移动平均窗口大小,差分次数]
    #移动平均主要采用差分的方法实现，主要针对存在周期性的数据，
    # 若不存在周期性，d=[1]    一阶差分
    #               d=[1,1]  二阶差分
    #==============================
    def diff_ts(self,ts, d):
        global shift_ts_list
        #  动态预测第二日的值时所需要的差分序列
        global last_data_shift_list
        #global predict_shift_list
        foreast_shift_list=[]
        shift_ts_list = []
        last_data_shift_list = []
        tmp_ts = ts
        for i in d:

            last_data_shift_list.append(tmp_ts[-i])

            shift_ts = tmp_ts.shift(i)
            shift_ts_list.append(shift_ts)
            tmp_ts = tmp_ts - shift_ts
            foreast_shift_list.append(tmp_ts[-1])
        foreast_shift_list[1:]=foreast_shift_list[0:len(foreast_shift_list)-1]
        foreast_shift_list[0]=ts[-1]

        tmp_ts.dropna(inplace=True)

        return tmp_ts,foreast_shift_list

    # ==============================
    # 根据移动平均窗口(差分实现)和差分次数，对ARMA预测的结果进行还原
    # ==============================
    def predict_diff_recover(self,predict_value, d):
        if isinstance(predict_value, float):
            tmp_data = predict_value
            for i in range(len(d)):
                tmp_data = tmp_data + last_data_shift_list[-i - 1]
        elif isinstance(predict_value, np.ndarray):
            tmp_data = predict_value[0]
            for i in range(len(d)):
                tmp_data = tmp_data + last_data_shift_list[-i - 1]
        else:
            tmp_data = predict_value
            for i in range(len(d)):
                try:
                    tmp_data = tmp_data.add(shift_ts_list[-i - 1])
                except:
                    raise ValueError('What you input is not pd.Series type!')
            tmp_data.dropna(inplace=True)
        return tmp_data

    # ==============================
    # 根据BIC最小原则，选择最合适的p和q,生成模型
    # ==============================
    def proper_model(self, data_ts, maxLag):
        init_bic = sys.maxsize
        init_p = 0
        init_q = 0
        init_properModel = None
        for p in np.arange(maxLag):
            for q in np.arange(maxLag):
                model = ARMA(data_ts, order=(p, q))
                try:
                    results_ARMA = model.fit(disp=-1, method='css')
                except:
                    continue
                bic = results_ARMA.bic
                if bic < init_bic:
                    init_p = p
                    init_q = q
                    init_properModel = results_ARMA
                    init_bic = bic
        return init_bic, init_p, init_q, init_properModel

    # ============MAIN FUNCTION==================
    # 根据BIC,选择最合适的p,q 建立ARMA模型，对数据根据差分和移动平均处理后的数据，进行还原
    # parmas:
    #    original_ts: pd.Series
    #    d:list
    #        ex:[1]: 一阶差分
    #           [12,1]:先隔12个数据点进行差分，再进行差分。当值大于1时，主要处理周期性问题
    #    maxLag:int 对p,q 进行遍历寻优的最大范围,采用BIC准则
    #
    # ===========================================
    def train_model(self,original_ts,d,maxLag=2,is_save=False):
        ts=np.log(original_ts)
        diffed_ts,foreast_shift_list=self.diff_ts(ts,d=d)
        init_bic, p, q, model=self.proper_model(diffed_ts,maxLag=maxLag)
        #model=self.creat_model(diffed_ts,p,q)
        predict_ts=model.predict()
        diff_recover_ts=self.predict_diff_recover(predict_ts,d=d)
        log_recover_ts=np.exp(diff_recover_ts)
        log_recover_ts.dropna(inplace=True)
        if is_save==False:

            self.evaluate_error(log_recover_ts,original_ts)
        else:
            joblib.dump(model,"arma.model")
            f1=open('forest_shift_list.pkl','wb')

            pickle.dump(foreast_shift_list,f1,-1)
            f1.close()
        #return log_recover_ts,model,diffed_ts,predict_ts
    #==============================
    #预测未来predict_days天的值，通过测算误差,评估模型在样本外数据的表现
    #==============================
    def test_model(self,test_ts,predict_days=5):
        recover_pre_value=self.foreast_recover_ts(predict_days=predict_days)
        recover_pre_value=pd.Series(index=test_ts.index,data=recover_pre_value)
        self.evaluate_error(recover_pre_value,test_ts)
    # ==============================
    # 预测未来days的值,并将数据进行还原
    # ==============================
    def foreast_recover_ts(self,predict_days=1):
        model=joblib.load("arma.model")
        f1 = open('forest_shift_list.pkl','rb')
        foreast_recover_list = pickle.load(f1)
        f1.close()
        predict_value=model.forecast(predict_days)[0]

        recover_pre_value=[]
        for i in range(0,len(predict_value)):
            for j in range(0,len(foreast_recover_list)):
                if j==0:
                    foreast_recover_list[-1]=foreast_recover_list[-1]+predict_value[i]
                else:
                    foreast_recover_list[-j - 1] = foreast_recover_list[-j - 1] + foreast_recover_list[-j]
            recover_pre_value.append(foreast_recover_list[0])
        recover_pre_value=np.exp(recover_pre_value)
        return recover_pre_value
    # ==============================
    # 增加新的数据
    # ==============================
    def add_new_data(self,ts,data,type='day'):
        if type=='day':
            new_index=ts.index[-1]+relativedelta(days=1)
        elif type=='month':
            new_index=ts.index[-1]+relativedelta(months=1)
        else:
            new_index=ts.index[-1]+relativedelta(years=1)
        ts[new_index]=data
        return ts


if __name__ == '__main__':
    arma=ARMA_TS()
    ts=arma.read_data(path='AirPassengers.csv')
    arma.train_model(ts,d=[12,1],is_save=True)
    pre=arma.foreast_recover_ts(1)








