import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

"""Loading the Iris Dataset"""
df = pd.read_csv('iris.csv', skiprows=1, header = None, names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(
    df.head(10))