import matplotlib
matplotlib.use('agg')

import pandas as pd
from ggplot import *

def histplot_compare(data):

    df = pd.read_csv(data)
    drain1 = df[df.rain == 1]
    dnorain = df[df.rain == 0]

    gg = ggplot(df, aes('ENTRIESn_hourly')) + \
    geom_histogram(drain1,fill = "red", alpha = 0.2, binwidth=250)+ \
    geom_histogram(dnorain,fill = "blue", alpha = 0.2, binwidth=250) +\
    xlim(0, 6000) +\
    ylim(0, 8000) +\
    ggtitle("Histogram of ENTRIESn_hourly for rainy/nonrainy days") \
    + labs("ENTRIESn_hourly", "Frequency")
  
    return gg

if __name__ == "__main__":
    data = "turnstile_weather_v2.csv"
    image = "Histogram_RainVsNoRain_bin250_Resubmit.png"
    gg =  histplot_compare(data)
    ggsave(image, gg, width=11, height=8)
#    ggsave(image, gg)

#    print "Done"