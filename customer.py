"""This class stores the information related to customers."""
class Customer:

    def __init__(self,first_name,last_name,table_number):          #this method is created to set up the name and table for customer.
        self.first_name = first_name
        self.last_name = last_name
        self.table_number = table_number
        self.ordered = []   #this empty list is used to hold food names

    def show_customer(self):

        """This method is made to print customer information"""

        print("Customer " + self.first_name)
        print("Table" + str(self.table_number))
    def add_order(self,food_name): #to add food to list
        self.ordered.append(food_name)
        print(food_name + " added to the order!" )

        """Method to remove the certain item from order."""

    def remove_item(self):   #to remove specific item from the order.
        food = input("Food to be removed? :")

        #used basic if ,else loop
        if food in self.ordered:
            self.ordered.remove(food)       #this code helps to remove the food from list.
            print(food + "is removed.")
        else:

            #if the food is not in list then this code will be executed.

            print("The food was not found in your order.")

        """the code below is used to show all the food customer bought."""

    def view_receipt(self):
        while True:

            #error handling so the program doesn't crash

            try:
                choice = input("Would you like to see the receipt (Y/N): ")

                if choice.upper() == "Y":
                    print("\nReceipt for " + self.first_name)
                    for item in self.ordered:                         #for loop to print the items one by one.
                        print(item)
                    break

                elif choice.upper() == "N":
                    print("  ")
                    break

                else:
                    print("Invalid choice, please enter Y or N. ")
            except Exception as e:
                print("something went wrong: " + str(e))


