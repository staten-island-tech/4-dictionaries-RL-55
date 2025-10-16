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
SnowdinShop=(item1,item2,item3)
def shop():
    cart=[]
    x=0
    print("Hello, traveller. How can I help you?")
    while not x==1:
        for a in range(3):
            print(SnowdinShop[a]["name"])
        y=input("What would you like to buy: ")
        for b in range(3):
            if y==SnowdinShop[b]["name"]:
                for c in item1:
                    print(SnowdinShop[b][c])
                y=input("Are you sure? Yes or No ")
                if y=="Yes" or y=="yes":
                    print("Thanks for your purchase")
                    cart.append(SnowdinShop[b]["name"])
                    y=input("Buy or Exit ")
                    if y=="Buy" or y=="buy":
                        x=0
                    elif y=="Exit" or y=="exit":
                        x=1
                        print(f"You purchased {cart}")
            else:
                print("")
shop()