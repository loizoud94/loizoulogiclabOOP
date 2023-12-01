# cafe

# Practical Task

# I have pre-populated 'menu' with what I consider to be the five essential stock items for any cafe.
menu = ["coffee", "tea", "eggs", "bread", "vegetarian sausage"]
print("\nAccording to the inventory, these are the items you currently have in stock: \n" + str(menu)) # User can check to see if the menu/stock list is correct.
print()

user_amend = 0
while user_amend != 3: # option to amend the stock list before proceeding.
    print("Enter 1 to add an item.")
    print("Enter 2 to remove an item.")
    print("Enter 3 if you are satisfied the stock list is correct and complete.")
    print("Enter 4 if you would like to see the stock list to check. \n")
    try: # cope with any input that would cause an exception
        user_amend = int(input("Add/Remove/Continue/See List (1-4): "))
    except:
        print("\nInvalid input. Please enter a number between 1 and 4.\n")
        continue

    if user_amend == 1: # Add an item
        new_item = input("\nWhat item would you like to add? ")
        new_item = new_item.lower() # account for someone accidentally having caps lock on.
        if new_item in menu:
            print(f" \nSorry. We are unable to add {new_item} as this is already in the stock list.") # Prevent duplicated in the stock list.
        else:
            menu.append(new_item) # add item to list.
        print()
    
    elif user_amend == 2: # Remove an item
        if len(menu) == 4: # maintaining at least four items on the stock list.
            print("\nSorry. The stock list must contain at least four different items. You must add something before you can remove anything. \n")
        else:
            remove_item = input("\nWhich item would you like to remove? ")
            remove_item = remove_item.lower() # account for any case input
            if remove_item not in menu:
                print("\nThis item can't be removed because it isn't in the stock list. \n") # removes a possible exception
                continue
            menu.remove(remove_item)
            print()
        

    elif user_amend == 3: # Continue
        print()

    elif user_amend == 4: # See the stock list
        print()
        print(menu)
        print()

    else:
        print("Invalid input. Please enter a number between 1 and 4. \n") # maintain the integrity of the input choice.


stock = {} # Empty dictionary to allow user to input amount of stock for each item

for item in menu:
    item_stock = None # cope with any invalid input from user
    while item_stock is None: 
        try:
            item_stock = int(input(f"How many servings of {item} do you have? "))
        except ValueError:
            print("\nPlease input a valid integer.\n")
    stock[item] = item_stock

price = {} # Empty dictionary to allow user to input wholesale cost of each item
for item in stock:
    stock_price = None # cope with any invalid input from user
    while stock_price is None: 
        try:
            stock_price = float(input("What is the wholesale cost of one serving of {}? \t£".format(item)))
        except ValueError:
            print("\nPlease input a valid price.\n")
    price[item] = stock_price

print("Total value of each item in stock:")
values_list = [] # empty list to sum for total value at the end.
for item in menu:
    item_value = stock[item] * price[item]
    print(item + ":\t£" + str(item_value)) # printing individual values of each item.
    values_list.append(item_value) # populate the values list

stock_value = sum(values_list)
print("Total value of all stock: £" + str(stock_value)) # final value of all stock