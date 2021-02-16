import csv
import plotly.express as  px 
import numpy as np 

def getdatasource(data_path):
    icecream_sales = []
    colddrink_sale = []
    
    with open ("data.csv")  as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
             icecream_sales.append(float(row ["Temperature"]))
             colddrink_sale.append(float(row ["Ice-cream Sales"]))

    return{"x":icecream_sales,"y": colddrink_sale}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation in between the Temperature and Ice-cream Sales is ", correlation[0,1])        

def setup():
    data_path = "./data.csv"
    datasource = getdatasource(data_path)
    findcorrelation(datasource)

setup()    


        #fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales")
        #fig.show()