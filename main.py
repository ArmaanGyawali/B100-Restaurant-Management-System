"""This files helps user import the different classes ,manage tables, foods, and every other operations that can be done in restaurant.  """
"""These functions help users to import different classes from different files."""
from customer import Customer
from manager import Manager
from menu import all_foods, load_menu
from table import Table

load_menu()         #this is used to load the menu

all_tables = []
for i in range(1,16):    #This loop helps to create table from 1 to 15.
    all_tables.append(Table(i,4,"Clean","Standard"))
my_table = None  #variable to hold the current table user selects.

print ("           WELCOME TO HomeLikeFood           ")
print("Customer Registration")
fname = input("Enter your first name : ")
lname = input("Enter your last name : ")
while True: #Used while loop so program can run until user picks available table.
    try:
        print("\n Tables available from 1 to 15.")
        table_choice = int(input("Choose the table you will like to have : "))
        for t in all_tables:  # searching through the list to find a table user wants .
            if t.table_number == table_choice:
                if t.occupy():
                    my_table = t
                    break
        if my_table is not None:  #if this statement is true the table was found and successfully occupied.
            break
        else:
            print("This table is busy or doesn't exist select between 1 to 15.")
    except ValueError:
        print("Invalid input 'please enter the no'")  # used exception to stop program from crashing if user typed words instead of numbers.
customer1 = Customer(fname,lname,table_choice)
print(f"\nWelcome, {customer1.first_name} is now sitting at table no :  {customer1.table_number}" )

while True:      # this loop is created to make sure the user/customer can choose multiple options without the program closing until the user decides to do so.
    print("_" * 40)
    print("1. Show Menu")
    print("2. Update Menu / Add new Item")
    print("3. Take Order")
    print("4. Remove item from the order")
    print("5. Change table location ")
    print("6. View Receipt and Pay")
    print("7. Exit")
    print("_" * 40)
    user_choice = input("What will you like to do ? ")

    if user_choice == "1":    # it just displays the menu using for loop.
        print("\nAvailable food's")
        for food in all_foods:      #to show just first names for every food in menu
            print(f"{food.name}")
        print("_" * 40)
        full_menu = input("Do you like to watch all information about food ? (Y/N) :  ")
        if full_menu.upper() == "Y":
            print("Menu")
            for food in all_foods:
                food.view_menu()
                print("_" * 40)
        else:
            print(" Okay, Going back to home screen. ")


    elif user_choice == "2":         #allows user to add new food item and also stores it in the menu.txt file so user can order food afterwards.
        print("\nEnter the new food you will like to add")
        name = input("Enter the food name : ")
        price = input("Enter the price eg. 10 (NOTE : PLEASE DON'T INSERT € OR ANY EXTRA KEYWORDS. : " )
        portion = input("Choose the portion size (Small,Medium,Large) : ")
        info = input("Enter the food description: ")
        with open("menu.txt", "a") as file:           #this line is one of most imp line as it opens the file 'with open' and a append's the text to end of file.
            file.write(f"\n{name},{price},{portion},{info}")     #matching the added food exactly in a way menu.txt was written to ensure food was added in same format.
        print(f"{name} has been added to the permanent menu! ")
        print("Please restart the program to see the new item in menu!")

    elif user_choice == "3":   #to order food
        print("What will you like to have ?")
        print("Please enter the food name to add it and type 'done' to finish it.")
        while True: #this loop helps user stay in ordering system as long ask they want
            choosed_order = input("Add item or type('done') to exit: ")
            if choosed_order.lower()=="done":
                print("We have successfully took your order!")
                break       #this exits loop and goes back to 1-7 menu.
            customer1.add_order(choosed_order)
            with open("ordered_foods.txt", "a") as file:
                file.write(f"Table {customer1.table_number} ordered {choosed_order}.")
            print(f"Added {choosed_order}")

    elif user_choice =="4":          #this part lets user delete the order from what they choose.
        print(f"Order : {customer1.ordered}")      #display's the food that's in their bucket
        item_to_remove = input("what food will you like to remove? : ")
        found= False      #set found to false so it stays false until we find food in list
        for food in customer1.ordered:  # using for lop so we know food in list matches what user typed.
            if food.lower().strip() == item_to_remove.lower().strip():
                customer1.ordered.remove(food)
                print(f"{food} have been removed.")
                found = True
                break     # if we find the food in list break the loop
        if not found:     #if not display this print statement.
            print("The food was not found in order.")

    elif user_choice =="5":   #this option lets user change the table
        my_table.status ="Clean"    #first we set the old table back to empty so it gets free for other customers
        print(f"Table {my_table.table_number} is now empty.")
        try:
            new_table = int(input("Which table you will like to have? (1-15) : "))  # asking which table they want now
            for t in all_tables:
                if t.table_number == new_table:  # check if new table is empty
                    if t.occupy():  # updating 'my_table' to be the  new table
                        my_table = t
                        customer1.table_number = t.table_number  # updating the customers info so in bill it shows there new table no.
                        print(f"Customer have moved to table no {t.table_number}")
                        break
                    else:
                        print("Table Busy.")
        except ValueError:
            print("Please enter only numbers")


#if user choose the option 6 it's assigned to view the receipt and paying the bill and in this logic i have added  customer ,menu and manager together.
    elif user_choice =="6":
         #checking if customer ordered anything before processing if yes move to else block or display the print statement.

        if len(customer1.ordered) == 0:
            print("You haven't order anything ,Please order something first.")
        else:
            total = 0                 #initializing the total price to zero
            for my_food in customer1.ordered:               #going through each food name in customer's order list using for loop
                for item in all_foods:                 #comparing the ordered food from every food in menu
                    if my_food.lower().strip() == item.name.lower().strip():          #used lower() and strip() to ensure capital and small letter don't matter eg. 'momo' matches 'momo'/ 'MOMO'.
                        total = total + item.price
            manager1 = Manager(customer1.first_name,customer1.table_number,customer1.ordered,total)             #creating manager object
            manager1.happy_hour_discount()
            if manager1.money < 0:                #to make sure price doesn't go below zero .
                manager1.money = 0
            manager1.money = round(float(manager1.money),2 )
            manager1.payment_method()
            manager1.bill()
            customer1.view_receipt()
            print("Total to Pay: €"+ str(manager1.money))


# if user chooses option 7 then it just display this print statement.
    elif user_choice =="7":
        print("Hope you had great time!" + "\n")
        print("Have a great day, Goodbye 👋🏻! ")
        break



