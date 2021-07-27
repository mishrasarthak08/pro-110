import pandas as pd
import plotly.figure_factory as ff
import csv
import statistics
import random


d = pd.read_csv("medium_data.csv")
data = d["reading_time"].tolist()
#fig = ff.create_distplot([d["temp"].tolist()],["temperature"])
#fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)

print(mean)
print(stdev)

def randomsetofmean():
    dataset = []
    for i in range(0,100):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)

    mean2 = statistics.mean(dataset)
    stdev2 = statistics.stdev(dataset)
    return mean2

def showfigure(meanlist):
    df = meanlist
    figure = ff.create_distplot([df],["mean"],show_hist = False)
    figure.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = randomsetofmean()
        meanlist.append(setofmeans)

    mean = statistics.mean(meanlist)
    stdev = statistics.stdev(meanlist)
    print("mean of sampling distribution :-",mean)
    print("stdev of sampling distribution :-",stdev)

    showfigure(meanlist)

setup()

