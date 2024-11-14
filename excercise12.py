import numpy as np

#Aufgabe 1
M = np.array([3,2,1,4]).reshape(2, 2) #Matrix M

M_inv = np.linalg.inv(M) #Invertierte Matrix M

I = np.matmul(M_inv,M) #Multiplikation der Matrix mit ihrer Inversen

print(I)

#Aufgabe 2
A = np.array([7,5,-3,3,-5,2,5,3,-7]).reshape(3, 3)

r = np.array([16,-8,0]).reshape(3, 1)

A_inv = np.linalg.inv(A) #Invertierte Matrix A

b = np.matmul(A_inv, r) #Invertierte Matrix A * r

print(b)
