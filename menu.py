"""Class to manage food items on menu."""
class menu:
    def __init__(self, name ,price,info,portion):
        #Giving the name,cost,details and portion of food
        self.name = name
        self.price = price
        self.info = info
        self.portion = portion
    def view_menu(self):
        """Printing the details of the food."""
        print("item : " + self.name)
        print("price : €" + str(self.price))
        print("info : " + self.info)
        print("portion : " + self.portion)
    def add_order(self):
        """asks input to user about what they want to order."""
        added = input("What will you like to have ")
        print(added)
    def update_price(self):  # this method helps staff to change the price of the item.
        new_price = input(f"Enter the new price of item {self.name}")
        self.price = new_price #saves the price to the new item
        print("The new price is €" + str(self.price))
all_foods = []    #list to store all the food
def load_menu():
    """This helps us to read the menu.txt file we created """
    all_foods.clear()
    try:
        with open("menu.txt", "r") as file:   #opening the file and reading the data
            for item in file:
                if item.strip():
                 data = item.strip().split(",")  # splitting the line by commas
                 new_food = menu(data[0], int(data[1]), data[3], data[2])  #to create the new food and add to list
                 all_foods.append(new_food)   #used append to add new food in our existing list

    except FileNotFoundError:
        #if the file is missing display this error
        print("Error : File 'menu.txt' was not found")
    except ValueError:
        #this is exception to catch the value error i.e. if price is not a number
        print("Price formatting incorrect in menu.txt")
load_menu()

