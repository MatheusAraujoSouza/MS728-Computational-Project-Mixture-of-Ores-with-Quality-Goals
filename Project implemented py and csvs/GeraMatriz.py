import random
import csv

def createCSV(name, header, val):

    with open(name, "w", encoding="UTF8") as f:

        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(val)

header1 = ["Elemento químico", "Teor Mínimo Permitido", "Meta", "Teor Máximo Permido"]
header2 = ["Pilha", "Fe (%)", "Al2O3 (%)", "P (%)", "PPC (%)", "He (%)", "Massa (ton)"]
header3 = ["Criterio", "-", "I", "MI", "C", "MC"]
header4 = ["Parâmetro", "Fe", "Al2O3", "P", "PPC", "He"]

val1 = [["Fe (%)", 44.5, 47.0, 49.5],
        ["Al2O3 (%)", 0.27, 0.32, 0.37],
        ["P (%)", 0.035, 0.040, 0.043],
        ["PPC (%)", 2.05, 2.35, 2.65],
        ["He (%)", 38, 40, 50]]

# Primeira Tabela
createCSV("PrimeiraTabela.csv", header1, val1)

# Segunda tabela
tam = 15
pilha = []
feVec, alVec, pVec, ppcVec, heVec, massVec = [], [], [], [], [], []

for i in range(0, tam):

    pilha.append(i + 1)
    feVec.append(round(random.uniform(39.90, 53.03), 3))
    alVec.append(round(random.uniform(0.16, 0.96), 3))
    pVec.append(round(random.uniform(0.031, 0.090), 3))
    ppcVec.append(round(random.uniform(0.64, 5.08), 3))
    heVec.append(random.randint(0, 99))
    massVec.append(random.randint(900, 2000))

dadosTab2 = [[]]

dadosTab2[0] = [1, feVec[0], alVec[0], pVec[0], ppcVec[0], heVec[0], massVec[0]]

for i in range(1, tam):

    aux = []
    aux.append(i + 1)
    aux.append(feVec[i])
    aux.append(alVec[i])
    aux.append(pVec[i])
    aux.append(ppcVec[i])
    aux.append(heVec[i])
    aux.append(massVec[i])

    dadosTab2.append(aux)

    del(aux)

createCSV("SegundaTabela.csv", header2, dadosTab2)

#Terceira Tabela

dadosTab3 = [[]]

dadosTab3[0] = ["Peso do critério"] + [0, 1, 5, 10, 100]
dadosTab3.append(header4)
dadosTab3.append(["Critério"] + ["MI", "-", "MC", "C", "-"])

"""" De forma automatizada

dadosTab3[0] = ["Peso do critério"] + random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), 
                   random.randint(0, 100), random.randint(0, 100)

dadosTab3.append(header4)

dadosTab3.append(["Critério"] + [header3[random.randint(1, 5)], header3[random.randint(1, 5)], header3[random.randint(1, 5)],
                 header3[random.randint(1, 5)], header3[random.randint(1, 5)]])"""

createCSV("TerceiraTabela.csv", header3, dadosTab3)

# Quarta Lista

dadosTab4 = ["Peso de comparação"] + [1, 100, 1000, 10, 1]

# dadosTab4 = ["Peso de comparação"] + [random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000)]

with open("QuartaTabela.csv", "w", encoding="UTF8") as f:

    writer = csv.writer(f)
    writer.writerow(header4)
    writer.writerow(dadosTab4)