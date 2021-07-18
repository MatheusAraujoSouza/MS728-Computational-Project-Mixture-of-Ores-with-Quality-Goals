import gurobipy as gp
from gurobipy import GRB
import csv
import pandas 
import numpy as np


df1 = pandas.read_csv('x.csv')
df2 = pandas.read_csv('xreal.csv')
#df3 = pandas.read_csv('df2real.csv')
df4 = pandas.read_csv('df2.csv')
df3 = pandas.read_csv('df2real.csv')

def weighted_average_m1(distribution, weights):
    return round(sum([distribution[i]*weights[i] for i in range(len(distribution))])/sum(weights),2)

    weighted_average_m1(distribution, weights)
    
print(df1)
print(df4.iloc[:,1])
resultado = np.zeros((5, 1))

for i in range(5):
    resultado [i,0]= weighted_average_m1(df4.iloc[:,i+1],df1.iloc[:,1])
print(resultado )


Elementos=list()
Elementos=['Fe (%)','Al2O3 (%)', 'P (%)', 'PPC (%)', 'He (%)']

Qui=dict()
for idx, valor in enumerate(resultado):
    rotulo=Elementos[idx]
    Qui[rotulo]=valor
print(Qui)

print(df4)







#df2 = pandas.read_csv('xreal.csv')
#df3 = pandas.read_csv('df2real.csv')
resultados2=resultado = np.zeros((5, 1))
for i in range(5):
    resultados2 [i,0]= weighted_average_m1(df3.iloc[:,i+1],df2.iloc[:,1])
print(resultados2 )
print("***********************")
print(df3)
print(df2)


Qui2=dict()
for idx, valor in enumerate(resultados2):
    rotulo=Elementos[idx]
    Qui2[rotulo]=valor
print(Qui2)


Qui = pandas.DataFrame.from_dict(Qui, orient='index')
Qui2 = pandas.DataFrame.from_dict(Qui2, orient='index')




print("valores gerados",Qui)
print("\n\nValores reais",Qui2)


'''
Qui.to_csv("mediaprealelatorio.csv")
Qui2.to_csv("mediapalreal.csv")
'''