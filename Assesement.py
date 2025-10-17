def englishorfrench():
    x=input("Write a sentence. ")
    y=0
    z=0
    for i in x:
        if i=="t" or i=="T":
            y=y+1
        elif i=="s" or i=="S":
            z=z+1
    if y>=z:
        print("French")
    else:
        print("English")

def occupied():
    w=int(input("Parking spaces "))
    x=input("Write . for empty C for occupied: ")
    y=input("Write . for empty C for occupied: ")
    z=0
    for i in range(w):
        if x[i]==y[i]=="C":
            z=z+1
    print(f"Occupied space for both days: {z}")
occupied()