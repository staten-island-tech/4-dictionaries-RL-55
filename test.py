item1 = {
    "name": "Bisicle",
    "price":"15G",
    "effect":"11HP",
    "desciption":"It's a two-pronged popsicle, so you can eat it twice."
    }
item2={
    "name":"Cinnamon Bunny",
    "price":"25G",
    "effect":"22 HP",
    "desciption":"A cinnamon roll in the shape of a bunny."
    }
item3={
    "name":"Manly Bandanna",
    "price":"50G",
    "effect":"7 DF",
    "desciption":"It has seen some wear. It has abs drawn on it."
    }
SnowdinShop=(item1,item2,item3,"Exit")
def shop():
    cart=[]
    x=0
    print("Hello, traveller. How can I help you?")
    while not x==1:
        for i in range(3):
            print(SnowdinShop[i]["name"])
        y=input("What would you like to buy? ")
        if y=="Bisicle":
            for h in item1:
                print(SnowdinShop[0][h])
            z=input("Are you sure? ")
            if z=="Yes":
                print("Thanks for your purchase.")
                cart.append(item1["name"])
            else:
                print("Just looking?")
        elif y=="Cinnamon Bunny":    
                    for h in item1:
                print(SnowdinShop[0][h])
            z=input("Are you sure? ")
            if z=="Yes":
                print("Thanks for your purchase.")
                cart.append(item1["name"])
            else:
                print("Just looking?")            
        elif y=="Manly Bandanna":
                        for h in item1:
                print(SnowdinShop[0][h])
            z=input("Are you sure? ")
            if z=="Yes":
                print("Thanks for your purchase.")
                cart.append(item1["name"])
            else:
                print("Just looking?")
        elif y=="Exit":
            print("Bye now! Come again sometime!")
            print(f"You bought{cart}")
            x=1

shop()