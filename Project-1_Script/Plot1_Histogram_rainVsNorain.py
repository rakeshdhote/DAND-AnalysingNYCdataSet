import matplotlib
matplotlib.use('agg')

import pandas as pd
from ggplot import *

def histplot_compare(datan):

    df = pd.read_csv(datan)
    xvar = df['ENTRIESn_hourly']
    
    gg = ggplot(aes(xvar, fill='rain', color='rain',label='rain'), data=df) \
    + geom_histogram(alpha=0.6,binwidth = 250) + ggtitle("Histogram of ENTRIESn_hourly for rainy/nonrainy days") \
    + labs("ENTRIESn_hourly", "Frequency")  #+ xlim(0, 5000)   
  
    return gg

if __name__ == "__main__":
    data = "turnstile_weather_v2.csv"
    image = "Histogram_RainVsNoRain22.png"
    gg =  histplot_compare(data)
    ggsave(image, gg, width=11, height=8)
#    ggsave(image, gg)

#    print "Done"