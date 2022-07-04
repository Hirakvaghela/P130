import csv
import pandas as pd

df = pd.read_csv("starFinal.csv")
print(df.shape)



df.to_csv("FinalFinal.csv")