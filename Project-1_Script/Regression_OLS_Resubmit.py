# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 13:23:19 2015

@author: Rakesh
"""
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

## 
def normalize_features(array):
   """
   Normalize the features in our data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

##########################################################
def Regression_OLS(features, values):
    
    x = features
    x = sm.add_constant(x) # add the first column as 1
    y = values
	
    # Linear regression
    model = sm.OLS(y, x)
    results = model.fit()

    return results

##########################################################
if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename) # read csv file

	# Extract the features and values from dataframe	
    features = turnstile_master[['rain','hour','weekday']]
    # Add UNIT to features using dummy variables
    dummy_units = pd.get_dummies(turnstile_master['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    features, mu, sigma = normalize_features(features)
    
    values = turnstile_master[['ENTRIESn_hourly']] 
	
	# Call to Regression function
    results = Regression_OLS(features,values)
    #dir(results)

    print results.summary() 
    print 'Parameters: ', results.params 
    print 'R2: ', results.rsquared     
    print 'R3: ', results.resid 
    
    residualP  = turnstile_master['ENTRIESn_hourly'] - results.predict()
    
    # Plot Linear Regression Diagonostics
    fig1 = plt.figure(num=1, figsize=(14, 12), dpi=80, facecolor='w', edgecolor='k')    
    # Residual plot
    plt.subplot(2, 2, 1)
    plt.plot(results.predict(),results.resid,'.')
    plt.grid(True)
#    plt.axis([1500, 2000, -10000, 25000]) 
    plt.xlabel('Fitted Data',fontsize=14, color='black')
    plt.ylabel('Residual',fontsize=14, color='black')
    plt.title(r'Residual Plot ',fontsize=14, color='black')

    # Residual plot - Closeup plot
    plt.subplot(2, 2, 2)
    plt.plot(results.predict(),results.resid,'.')
    plt.grid(True)
    plt.axis([1500, 1600, -5000, 5000]) 
    plt.xlabel('Fitted Data',fontsize=14, color='black')
    plt.ylabel('Residual',fontsize=14, color='black')
    plt.title(r'Residual Plot (close-up)',fontsize=14, color='black')    

    # Residual plot - Closeup plot
    plt.subplot(2, 2, 3)
    plt.plot(values,results.predict(),'.')
    plt.grid(True)
#    plt.axis([1500, 1600, -5000, 5000]) 
    plt.xlabel('Original Data',fontsize=14, color='black')
    plt.ylabel('Fitted Data',fontsize=14, color='black')
    plt.title(r'Fitted Vs Original data',fontsize=14, color='black')    
    
    # Q-Q plot
    plt.subplot(2, 2, 4)    
    stats.probplot(results.resid,fit=True,plot=plt)
    plt.grid(True)
    
    plt.savefig('LRDiagonistic.jpg')
    
    
    
    
    
    
    
    
    
    