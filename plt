df=pd.concat([d1,d2,d3,d4],axis=0)
df=df.groupby('region').mean()['avg_pr_hour']


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['axes.spines.top']=False
plt.rcParams['axes.spines.right']=False


plt.rcParams['ytick.labelsize']=16
plt.rcParams['xtick.labelsize']=16



data2.plot(kind = 'bar', figsize=(10,4), color= ['steelblue']) #color='steelblue'  #, colormap = 'summer_r')  ,ylim=(0,2250)

plt.xlabel("Region",fontsize=18) #X轴标签  
plt.ylabel("Claim数量",fontsize=18)  #Y轴标签  
#添加文字
for x, y in enumerate(data2.values):
    plt.text(x-0.1, y+150, "%1.0f" %y,fontsize=16) #带百分号时 %y+'%'

    
scale_ls = range(4)
_ = plt.xticks(scale_ls,list(data2.index),rotation=0,fontsize=17)


plt.plot(df.index, df.values*365, color='black', marker='*', ms=10, label="年均降水量")  #marker='*'
plt.legend(fontsize=16,loc='best')


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['axes.spines.top']=False
plt.rcParams['axes.spines.right']=False


plt.rcParams['ytick.labelsize']=16
plt.rcParams['xtick.labelsize']=16



data2.plot(kind = 'bar', figsize=(16,8),ylim=(0,2250), color= ['steelblue']) #color='steelblue'  #, colormap = 'summer_r')

#plt.xlabel("月份",fontsize=18) #X轴标签  
#plt.ylabel("Claim数量",fontsize=18)  #Y轴标签  
#添加文字
for x, y in enumerate(data2.values):
    plt.text(x-0.3, y+15, "%1.0f" %y,fontsize=16) #带百分号时 %y+'%'


scale_ls = range(31)
_ = plt.xticks(scale_ls,list(data2.index),rotation=50,fontsize=17)


#plt.plot(all_rain.index, all_rain.values/100, color='black', marker='*', ms=10, label="降水量")  #marker='*'





a2=pd.DataFrame()
#a2['3 days before']=[0.5399,0.3832,0.0548,0.0146,0.0033,0.0028,0.00119]
#a2['7 days before']=[0.3362,0.6023,0.0500,0.0091,0.0016,0.0005,0.0]

#Eliminate no rainfall
a2['前7天']=[0.7410,0.1666,0.0560,0.0193,0.0137,0.0033]
a2['前3天']=[0.6561,0.1768,0.0814,0.0378,0.0318,0.0161]



# 多系列柱状图
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['axes.spines.top']=False
plt.rcParams['axes.spines.right']=False


plt.rcParams['ytick.labelsize']=16
plt.rcParams['xtick.labelsize']=16


a2.plot(kind = 'bar',figsize=(12,6), ylim=(0,0.8),color= ['steelblue','grey']) #color='steelblue'  #, colormap = 'summer_r') grid = True,



plt.xlabel("平均日降水量(单位: mm)",fontsize=18) #X轴标签  
plt.ylabel("车辆占比",fontsize=18)  #Y轴标签  



def to_percent(temp, position):
    return '%1.0f'%(100*temp) + '%' #坐标轴分位数显示

plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
#plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

#添加文字
#for x, y in enumerate(a2['3 days before'].values):
#    plt.text(x-0.3, y+0.01, "%0.1f" %(y*100)+'%',fontsize=16) #带百分号时 %y+'%'
    
#for x, y in enumerate(a2['7 days before'].values):
#    plt.text(x+0.1, y+0.01, "%0.1f" %(y*100)+'%',fontsize=16) #带百分号时 %y+'%'
    

#5 10 15 20 30
scale_ls = range(6)
_ = plt.xticks(scale_ls,['1-5','6-10','11-15','16-20','21-30','More Than 30'],rotation=0,fontsize=16)
    
#plt.text(2, 750, 'TMc',fontsize=16)
plt.legend(fontsize=16,loc='best')

plt.plot(a2.index, a2['前7天'].values, color='steelblue', marker='*', ms=10, label="a") # "r", marker='*', #a2['3 days before'].values,
plt.plot(a2.index+0.25, a2['前3天'].values, color='grey', marker='*', ms=10, label="a") 
