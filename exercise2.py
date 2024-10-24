# 2)
def teilbar(x, y):
    if y == 0 :
        print("Es ist nicht möglich durch 0 zu teilen!")
    elif x == y:
        print("x und y sind gleich.")
    else:
        if x%y == 0:
            print("x ist durch y teilbar")
        else:
            print("x ist nicht durch y teilbar")
        
teilbar(4, 4)   
        
    
    

