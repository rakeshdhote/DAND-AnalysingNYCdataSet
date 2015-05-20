import matplotlib
matplotlib.use('agg')
import pandas as pd
import pandasql
import matplotlib.pyplot as plt
import numpy as np
import datetime
###############################################################################
def plotd(datan):
    
    #read dataframe
#    df = pd.read_csv(data)
    df = pd.read_csv(datan)
    df['datet'] = df['DATEn']+' ' + df['TIMEn']
    df['weekday06'] = pd.DatetimeIndex(df['datet']).weekday
   
    # extract data for plotting
    q = """
    SELECT hour, AVG(ENTRIESn_hourly) 
    FROM df 
    GROUP BY hour, weekday06
    """
    solution = pandasql.sqldf(q.lower(), locals())
    solution

    # Extracting Day and average hourly entries for different dates in x and y
    x = np.array(range(0,7)).T
#    x = np.array(['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat','Sun']).T    
    y = np.array(solution)[:,[1]]
   
    y1 = y[0:7] # 00:00 hrs
    y2 = y[28:35] # 16:00 hrs
    y3 = y[35:42] # 20:00 hrs
    
    # plotting figure
    figu = 1
    fig1 = plt.figure(num=1, figsize=(12, 8), dpi=250, facecolor='w', edgecolor='k')    
    
#    plt.plot(x, y[0:7], '-ro', x, y[7:14], '-gv', x, y[14:21], '-k^',\
#    x, y[21:28], '-c*',x, y[28:35], '-mx',x, y[35:42], '-bD',linewidth=2.0)
    plt.plot(x, y1, '-ro', x, y2, '-gv', x, y3, '-bD', linewidth=2.0)
    
    plt.xticks([0,1,2,3,4,5,6], ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat','Sun'],fontsize=18)
    plt.yticks(fontsize=18)


    plt.grid(True)
    plt.hold(True) # hold on  
    plt.xlabel('Weekday',fontsize=20, color='black')
    plt.ylabel('Average ENTRIESn_hourly',fontsize=20, color='black')
    plt.title(r'Average ENTRIESn_hourly at different times on weekdays'\
    ,fontsize=18, color='blue')
#    plt.xticks(range(1,32))
    plt.legend( ["time: 00:00 hr","time: 16:00 hr","time: 20:00 hr"],fontsize=16)
#    plt.axis([0, 39, 0, 4500])
    
    fig1.savefig('Avg_Entries_hourlyVsDay_Resubmit.png')
     
    return solution

###############################################################################    
if __name__ == "__main__":
    data = "turnstile_weather_v2.csv"
    plotdata =  plotd(data)


    
#    ax = plt.subplot(111)
#    ax.bar(x-0.2, y1,width=0.2,color='b',align='center')
#    ax.bar(x, y2,width=0.2,color='g',align='center')
#    ax.bar(x+0.2, y3,width=0.2,color='r',align='center')
#    plt.show()
#    ax.set_xticklabels('Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat','Sun')
#    
#    plt.xticks([0,1,2,3,4,5,6], ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat','Sun'],fontsize=18)
#    
#    
#    
#    plt.bar(x,y[0:7])
    
    
    
    
    