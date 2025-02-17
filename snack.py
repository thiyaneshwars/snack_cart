
items = {"Lays ":"₹5.00",
         "Hide and Seek ":"₹20.00",
         "Borbun :"₹20.00",
         "Oreio ":"₹50.00",
         "Good day ":"₹15.00",
         "Bottled Water ":"₹12.00"}

price = []
food =[]
for keys,values in items.items():
    print(f"{keys}:{values}")

while True:
    list = input("Enter the listed item you wants to buy :(press q to exit)")

    found_item = next((key for key in items if key.lower() == list.lower()), None)


    if found_item:
        print(f"{list} is added to  your cart")
        price.append(items[found_item])
        value = items.values()
        food.append(found_item)

    elif list.lower() == 'q':
        print(f"Thank you for shopping with us just enjoy you snack {food}")
        break

    else:
        print("Sorry we don't have that item")
    


total = sum(float(i.split('$')[1])for i in price)
    
print (f"your total amount is $ {total:.2f} ")
