import pandas.io.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

day=datetime.timedelta(days=1)
today=datetime.datetime.date(datetime.datetime.now())
t=int(input('Podaj liczbe dni kalendarzowych z ktorych pobrac dane:  '))
st=datetime.datetime.date(datetime.datetime.now())-t*day
shift=int(input('Podaj parametr dla RSI: '))

dax=web.get_data_yahoo('^GDAXI',start=st,end=today)

dax['rsi']=0.0
updays=[]
downdays=[]
day_diff_index={}

for i in range(len(dax)):
    day_diff_index[i]=dax['Close'][i]-dax['Open'][i]
      
for j in range(shift):
    if day_diff_index[j]>=0.0 :
        updays.append(day_diff_index[j])
    else:
        downdays.append(day_diff_index[j])    
        
for k in range(shift,len(dax)):
    if day_diff_index[k-shift]>=0.0 :
        del updays[0]
    else:
        del downdays[0]
    
    
    if day_diff_index[k]>=0.0 :
        updays.append(day_diff_index[k])
    else:
        downdays.append(day_diff_index[k])

    x=abs(sum(downdays))     
    if x==0.0:
        x=1.0
  

    dax['rsi'][k]=100.0-100.0/(1.0+(sum(updays)/x))


fig=plt.figure(figsize=(16,10))

a=plt.subplot2grid((3,1),(0,0),rowspan=2)
dax['Close'].plot(color='k')
a.grid(True)

b=plt.subplot2grid((3,1),(2,0),axisbg='lightgrey')
dax['rsi'].plot(color='b')
b.grid(True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
