# 1a)
def cagr_berechnung(AK, EK, t):
    AK = abs(AK)
    EK = 700
    t = abs(t)
    cagr = ((EK/AK)**(1/t)-1)
    return cagr

print(cagr_berechnung(100, 700, 30))


# 1b)
rendite = cagr_berechnung(100, 700, 30)

print(120 * (1 + rendite)**30)

    
