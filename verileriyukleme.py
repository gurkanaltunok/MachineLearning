import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('veriler.cvs')

#print(veriler)

boy = veriler[["boy"]]

#print(boy)

boykilo = veriler[["boy","kilo"]]

#print(boykilo)

l = []

foreach boylar in boy:
    print(boylar)


