x=input("Write a sentence. ")
y=0
z=0
for i in x:
    if i=="t" or i=="T":
        y=y+1
    elif i=="s" or i=="S":
        z=z+1
if y>=z:
    print("English")
else:
    print("French")