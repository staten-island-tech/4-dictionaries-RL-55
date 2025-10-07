item1 = {
    "name": "Bisicle",
    "price":"15G",
    "effect":"11HP",
    "description":"It's a two-pronged popsicle, so you can eat it twice."
    }
item2={
    "name":"Cinnamon Bunny",
    "price":"25G",
    "effect":"22 HP",
    "description":"A cinnamon roll in the shape of a bunny."
    }
item3={
    "name":"Manly Bandanna",
    "price":"50G",
    "effect":"7 DF",
    "description":"It has seen some wear. It has abs drawn on it."
    }
SnowdinShop=(item1,item2,item3)
def shop():
    cart=[]
    x=0
    print("Hello, traveller. How can I help you?")
    while not x==1:
        for i in range(2):
            print(SnowdinShop[i+1]["name"])
        y=input("What would you like to buy? ")
        if y=="Bisicle":
            print(item1)
            z=input("Buy? Yes,No ")
            if z=="Yes":
                print("Thanks for your purchase.")
                cart.append(item1)
        elif y=="Cinnamon Bunny":
            print(item2)
        elif y=="Manly Bandanna":
            print(item3)
        else:
            print("That is not in my shop.")
shop()