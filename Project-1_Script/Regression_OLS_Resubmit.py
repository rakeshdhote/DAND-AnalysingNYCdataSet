# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 13:23:19 2015

@author: Rakesh
"""
import pandas as pd
import statsmodels.api as sm

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

    print results.summary() 
    print 'Parameters: ', results.params 
    print 'R2: ', results.rsquared     
    print 'R3: ', results.resid 
