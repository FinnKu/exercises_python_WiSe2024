import numpy as np

y = np.array([2,3,8,4,10,1,9,5,1,0])


y_std = np.sqrt(1/len(y) * np.sum((y - np.mean(y))**2)) # Ganze Formel



y_stdd = np.std(y) # Gleiches Ergebnis wie oben, bloß mit der Funktion aus Numpy.


print(y_std)
print(y_stdd)
