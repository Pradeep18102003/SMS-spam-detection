#importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset

df = pd.read_csv('spam.csv', encoding= 'Latin-1')
df = df.dropna(how= 'any', axis=1)
df.columns = ['target', 'message']
print(df.head())