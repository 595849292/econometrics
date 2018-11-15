# coding=utf-8
import numpy as np
import math
import scipy.stats
#===========================
#计算给定滞后项 的自相关系数
#===========================
def autocorrelation(rt,lag):
    if lag<0 or lag>=len(rt)-1:
        raise Exception('Lag is out of range')
    rt[1:]=rt
    avg_r=np.array(rt).mean()
    numerator=0
    denominator =0
    for t in range(lag+1,len(rt)):
        numerator=numerator+(rt[t]-avg_r)*(rt[t-lag]-avg_r)
    for t in range(1,len(rt)):
        denominator=denominator+(rt[t]-avg_r)*(rt[t]-avg_r)
    p_lag=numerator/denominator
    return p_lag
#============================
#检验自相关系数是否显著为0(t检验)
#============================
def t_test(rt,lag,alfa):
    p_lag=autocorrelation(rt,lag)
    p_lag_sq=0
    for i in range(1,lag):
        r=autocorrelation(rt,i)
        p_lag_sq=p_lag_sq+r*r
    t_value=p_lag/math.sqrt((1+2*p_lag_sq)/len(rt))
    threshold=scipy.stats.norm.isf(1-alfa/2)
    if abs(t_value)>threshold:
        return str(lag)+'阶滞后下收益率序列显著相关，即序列不平稳'
    else:
        return str(lag) + '阶滞后下收益率序列显著不相关，即序列平稳'
#=============================
#联合检验（F检验）＃Empically,m=Ln(T)
#=============================
def f_test(rt,alfa,m):
    T=len(rt)
    p_sum=0
    for i in range(1,m+1):
        r=autocorrelation(rt,i)
        p_sum=p_sum+r*r/(T-i)
    Q=T*(T+2)*p_sum
    threshold=scipy.stats.chi2.isf(1-alfa,df=m)
    if Q>threshold:
        return '联合检验收益率不显著都为0'
    else:
        return '联合检验收益率显著都为0'
if __name__ == '__main__':
    a=scipy.stats.chi2.isf(0.95,df=2)
    print(a)

