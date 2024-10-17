p = 100
t = 10
i = 0.03

A = p*(1+i)**t

print(A)


p_b = 1
n = 365*24*60
i_b = 1
t = 1

B = p_b*(1+i_b/n)**n*t

print(B)