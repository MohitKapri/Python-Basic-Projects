menu = {
     "Pizza" : 100,
     "Momo" : 80,
     "Choumine" : 50,
     "Burger" : 60,
     "Spring roll" : 70,
}

print("WELCOME TO OUR CAFE")
print("Pizza:Rs-100\nMomo:Rs-80\nChoumine:Rs-50\nBurger:Rs-60\nSpring roll:Rs-70")

order_total = 0 

item_1 = input("Enter the name of the item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to list of your order!")
else:
    print("The item you want to order is currently unavaliable in our cafe")

another_item = input("Do you want to add another thing to your list? (Yes/No) :")
if another_item =="Yes":
    item_2 = input("Enter the item you want to add to your order = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to the list you want to order!")
    else:
        print("The item you want to order is currently unavaliable in our cafe")

print(f"The amount you have to pay is {order_total}")
