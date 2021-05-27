import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import csv
import pandas as pd 
import random 

df=pd.read_csv("medium_data.csv")
data=df[""].tolist()

mean=statistics.mean(population_mean)
print("mean is -->",mean)

mean_list=[]

def random_set_of_mean(30):
    dataset=[]
    for i in range(0,30):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
        set_of_means=random_set(1000)
        mean_list.append(set_of_means)

    