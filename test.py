SnowdinShop={
"1" : {
    "name": "Bisicle",
    "price":15,
    "effect":"11HP",
    "desciption":"It's a two-pronged popsicle, so you can eat it twice."},
"2":{
    "name":"Cinnamon Bunny",
    "price":25,
    "effect":"22 HP",
    "desciption":"A cinnamon roll in the shape of a bunny."},
"3":{
    "name":"Manly Bandanna",
    "price":50,
    "effect":"7 DF",
    "desciption":"It has seen some wear. It has abs drawn on it."}
}
def shop():
    cart=[]
    off=0
    G=0
    print("Hello, traveller. How can I help you?")
    while not off==1:
        for a in SnowdinShop:
            print(SnowdinShop[a]["name"])
        y=input("What would you like to buy: ")
        for b in SnowdinShop:
            if y==SnowdinShop[b]["name"]:
                for c in SnowdinShop["1"]:
                    print(SnowdinShop[b][c])
                y=input("Are you sure? Yes or No ")
                if y=="Yes" or y=="yes":
                    print("Thanks for your purchase")
                    cart.append(SnowdinShop[b]["name"])
                    G+=SnowdinShop[b]["price"]
                    y=input("Buy or Exit: ")
                    if y=="Buy" or y=="buy":
                        off=0
                    elif y=="Exit" or y=="exit":
                        off=1
                        print(f"You purchased {cart}",f"Price: {G}G")
shop()