# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 09:23:19 2015

@author: Rakesh
"""
import numpy as np
import scipy.stats
import pandas as pd
###############################################################################
def compare_averages(filename):

    df = pd.read_csv(filename)

    dfrain = df[df.rain == 1]['ENTRIESn_hourly']
    dfnorain = df[df.rain == 0]['ENTRIESn_hourly']
            
    with_rain_mean = np.mean(dfrain)
    without_rain_mean = np.mean(dfnorain) 

    with_rain_median = np.median(dfrain)
    without_rain_median = np.median(dfnorain)     
    
    U, p = scipy.stats.mannwhitneyu(dfrain, dfnorain, use_continuity=True)

    x = dfrain
    y = dfnorain
    m_u = len(x)*len(y)/2
    sigma_u = np.sqrt(len(x)*len(y)*(len(x)+len(y)+1)/12)
    z = (U - m_u)/sigma_u
    pval = 2.*scipy.stats.norm.cdf(z)

    if p < 0.05:
        print 'Null Hypothesis (two population means are same) is rejected'               
        return (False, with_rain_mean, without_rain_mean, results)

    if p > 0.05:
        print 'Null Hypothesis (two population means are same) cannot be rejected'        
        return (True,with_rain_mean, without_rain_mean, results)
###############################################################################
if __name__ == '__main__':
    filename = "turnstile_weather_v2.csv"
    result = compare_averages(filename)
    print result
