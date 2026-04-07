"""Class that manages the table number ,table_status, location."""
class Table:
    def __init__(self,table_number,capacity,status,location):  #4 attributes
        self.table_number = table_number #to set up the table no e.g. table no 1
        self.capacity = capacity #to show how many people can sit in table
        self.status = status #to check if th table is clean or occupied
        self.location = location #to check the location of table inside shop

    """The method to check if the table is occupied or clean"""
    def occupy(self):
        try:
            # checking if the table is clean
            #used boolean(True/False) to control the flow of the program.
            if self.status == "Clean":
                #changing to occupied if it's clean.
                self.status = "Occupied"
                print(f"Table {self.table_number} is occupied.")
                return True
            else:
                #prints this if it's full or not clean
                print("This table is not clean!")
                return False
        except Exception as e:
            print(f"Error : {e}")
            return False

    """This method is used to change table status to clean"""
    def clean_table(self):
        self.status = "Clean"
        print("The table is cleaned.")

    """This method is used to change the location of table """
    def change_location(self):
        new_location = input("Where have customer moved to ? : ")
        self.location = new_location #this line updates the location
        print("Customers moved to " + self.location)



