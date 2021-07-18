#Problema da mochila
 
import gurobipy as gp
from gurobipy import GRB
import csv
import pandas 
import numpy as np

#Criando os dataframe dos dados 

df1 = pandas.read_csv('PrimeiraTabela.csv')
#df2 = pandas.read_csv('SegundaTabela.csv')
df2 = pandas.read_csv('SegundaTabelamod.csv')
df3 = pandas.read_csv('TerceiraTabela.csv')
df4 = pandas.read_csv('QuartaTabela.csv')
df5 = pandas.read_csv('valoresc.csv')



#SegundaTabelamod
print(df5)
print(df1)
print(df2)
print(df3)
print(df4)


############Sejam os seguintes dados de entrada para o problema################

#tlj: Teor mínimo admissível para o parâmetro j no produtonal (%)

tlj=dict()
for idx, valor in enumerate(df1["Teor Mínimo Permitido"]):
    rotulo=df1.iloc[idx]["Elemento químico"]
    tlj[rotulo]=valor
    
#trj : Teor desejável para o parâmetro j no produto final (%)
trj=dict()
for idx, valor in enumerate(df1["Meta"]):
    rotulo=df1.iloc[idx]["Elemento químico"]
    trj[rotulo]=valor
    
#tuj : Teor superior para o parâmetro j no produto final (%)
tuj=dict()
for idx, valor in enumerate(df1["Teor Máximo Permido"]):
    rotulo=df1.iloc[idx]["Elemento químico"]
    tuj[rotulo]=valor

# wdtj:Peso do desvio da meta para o parâmetro j
wdtj=dict()
wdtj={'Fe (%)': 1,'Al2O3 (%)': 100, 'P (%)': 1000, 'PPC (%)': 10, 'He (%)': 1}


#Qui: Quantidade máxima disponível na pilha i, em toneladas
index = df2.index

Qua=list()
for i in range(len(index)):
   Qua.append("Qua_{}".format(i+1))
   

Qui=dict()
for idx, valor in enumerate(df2["Massa (ton)"]):
    rotulo=Qua[idx]
    Qui[rotulo]=valor


#nunidreti: Número de unidades de retomada
unidreti=10

#tij : Teor do parâmetro j na pilha i (%)
Pilha=list()
for i in range(len(index)):
   Pilha.append("Pilha_{}".format(i+1))
   
Elementos=list()
Elementos=['Fe (%)','Al2O3 (%)', 'P (%)', 'PPC (%)', 'He (%)']

centro_df2 = np.zeros((len(Pilha), len(Elementos[0])-1))
for i in range(len(Elementos[0])-1):
    centro_df2[:,i]=df2.iloc[:,i+1]



Massa = np.zeros((len(Pilha), 1))
Massa[:,0]=df2.iloc[:,6]

print(df2)
print(Massa)

tij=dict()
for i in range(len(Pilha)):
    for j in range(len(Elementos[0]) - 1):
        rot_pilha = Pilha[i]
        rot_Elementos=Elementos[j]
        tij[rot_pilha,rot_Elementos] = centro_df2[i][j]
        
#p : Produção total requerida, em toneladas
p=6000

#retmin :  retomar um mínimo

retmin=500

#################################variáveis de decisão##########################

m=gp.Model()
y=m.addVars(Pilha,vtype=gp.GRB.BINARY)
x=m.addVars(Pilha,vtype=gp.GRB.CONTINUOUS)
dtpj=m.addVars(Elementos,vtype=gp.GRB.CONTINUOUS)
dtnj=m.addVars(Elementos,vtype=gp.GRB.CONTINUOUS)
nunidreti=m.addVars(Pilha,vtype=gp.GRB.INTEGER)








##########################Função objetivo###################################################

m.setObjective(gp.quicksum(wdtj[j] * dtnj[j] + wdtj[j] * dtpj[j] for j in Elementos) 
   , sense=gp.GRB.MINIMIZE)



       

##################################Restrições##############################################
c1=m.addConstrs(gp.quicksum(((tij[i,j] - tuj[j])*x[i]) for i in  Pilha) <= 0 for j in Elementos )

c2=m.addConstrs(gp.quicksum((tij[i,j] - tlj[j])*x[i] for i in  Pilha )>= 0 \
 for j in Elementos )

c3=m.addConstrs(gp.quicksum((tij[i,j] - trj[j])*x[i] for i in  Pilha ) \
 + dtnj[j] - dtpj[j]   == 0  for j in Elementos )
    
    
    
const=0   
for i in Pilha:
    c4=m.addConstr(x[i] <= Massa[const])
    const+=1


c5=m.addConstr(gp.quicksum(x[i] for i in Pilha) == 6000 )




c6=m.addConstrs((nunidreti[i] ==   x[i]/unidreti) for i in Pilha  )


c7=m.addConstrs((x[i] >= retmin*y[i]) for i in Pilha  )


    
const=0   
for i in Pilha:
    c8=m.addConstr(y[i] >= (x[i]/Massa[const]))
    const+=1


m.optimize()

print("Desvio negativo da meta para o parâmetro j, em toneladas\n\n",dtnj)
print("\n\nDesvio positivo da meta para o parâmetro j, em toneladas\n\n",dtpj)
print("\n\nPilhas selecionadas\n\n ",y)
print("\n\n valores pegos de cada pilha x\n\n",x)
print("\n\n Numero de unidades de retomada\n\n",nunidreti)
print("\n\nPrint atual\n\n")



############################Criating dataframes from data#####################


dfObj = pandas.DataFrame.from_dict(x, orient='index')
dfObj2 = pandas.DataFrame.from_dict(y, orient='index')
dfObj3 = pandas.DataFrame.from_dict(dtnj, orient='index')
dfObj4 = pandas.DataFrame.from_dict(dtpj, orient='index')
dfObj5 = pandas.DataFrame.from_dict(nunidreti, orient='index')





print("\n\nvalores pegos de cada pilha x\n")
print(dfObj)
print("\n\nPilhas selecionadas\n")
print(dfObj2)
print("\n\nDesvio negativo da meta para o parâmetro j, em toneladas\n")
print(dfObj3)
print("\n\nDesvio positivo da meta para o parâmetro j, em toneladas\n")
print(dfObj4)
print("\n\nNumero de unidades de retomada\n")
print(dfObj5)

print("\n\n Custo total ")
soma=1700.0 *  12.0 +10.0*660.0000000000039 + 550.0*11.5 + 850.0000000000081 * 12.0 + 990.0 * 12.3 + 12.1* 1249.9999999999882  



print(soma)
print('Optimal objective: %g' % m.objVal)    
    
'''



#############################Making csv from output#############################

dfObj.to_csv(" xreal.csv")
dfObj2.to_csv(" yreal.csv")
dfObj3.to_csv(" dtnjreal.csv")
dfObj4.to_csv(" dtpjreal.csv")
dfObj5.to_csv(" nunidretireal.csv")

#########################Making csv from input################################

#df1.to_csv("df1real.csv")
df2.to_csv("df2real.csv")
#df3.to_csv("df3real.csv")
#df4.to_csv("df4real.csv")
#df5.to_csv("df5real.csv")


'''