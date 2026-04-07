"""This class manages the receipt, discount, and also used to save the final receipt."""
class Manager:
    def __init__(self,name,table,items,money):  # setting up the basics like customer name, table number
        self.name = name
        self.table = table
        self.items = items
        self.money = money
    def bill(self):
        """to write the receipt into a  text file."""
        try:
            file = open("final_bill.txt", "w") # opening and writing a file
            file.write("---HOMELIKE FOOD RECEIPT---\n")
            file.write("Customer: " + self.name + "\n")
            file.write("Table: " + str(self.table)+ "\n")
            file.write("Total : €"  + str(self.money) + "\n")
            file.write("Orders: "+ str(self.items) + "\n")
            file.close()  # closing the file to save it properly.
            print("Bill saved to final_bill.txt")
        except Exception as e:
            print("Count not save the bill " + str(e)) #showing the error ,if there will be issue while saving the file ,
    def happy_hour_discount(self):
        """this method is used to add discount """
        discount =float(input("enter the  discount  you got ")) #using float so user can give decimal numbers.
        self.money = self.money - discount # subtracting
        print(f"The price after discount is {self.money}." )
    def payment_method(self):
        """this method handles the payment method """
        payment = input("Will you like to pay by Card or Cash? ")
        if payment =="Card":
            print("Please place your card on machine , Thank you !")
        else:
            print("Processing the payment, Thank you !")



