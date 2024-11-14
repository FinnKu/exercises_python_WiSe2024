import numpy as np

data = np.arange(1,11)

D = np.tile(data, 10) #Erstellt das Array

D = D.reshape(10, 10) # Gibt dem Array seine Form mit mehreren Dimensionen

print(D.sum(axis = 0)) # Summen aller Spalten

print(D.mean(axis = 1)) #Mittelwert der 