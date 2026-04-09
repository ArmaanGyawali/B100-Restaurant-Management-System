# B100-Restaurant-Management-System

This is my Python project for university. It is a system for a restaurant called "HomeLikeFood". I used Object-Oriented Programming (OOP) to build it . I have used basic loops, different classes with different attributes and objects and also i have shown use of exception handling to stop my program from crashing.

- What this program does:
1. Customer Registration: Asks for name and helps user pick a table from 1 to 15.
2. Menu System: Shows a list of food names. If the user wants, they can see full details like price and info.
3. Ordering: Users can order many items at once. They just type the food name and press enter. Type 'done' when finished.
4. Update Menu: The manager can add new food items to the 'menu.txt' file.
5. Billing: Calculates the total price, applies Happy Hour discounts, and saves the receipt to a file.

- Files in this project:
1. main.py - The main loop where the program runs.
2. customer.py - Handles customer names and their orders.
3. manager.py - Calculates the bill and discounts.
4. menu.py - Loads the food items from the text file.
5. table.py - Manages if a table is busy or free.
6. menu.txt - This is where the food data is stored.
7. final_bill.txt - This is the file that get created after the bill it printed to save the receipt.

- How to use:
1. Download all files into the same folder.
2. Open your terminal or VS Code.
3. Run the command: 'python main.py'
4. Follow the instructions on the screen!

- Example Usage
Based on a session:
1.  Start: Enter first name (eg. "Armaan") last name (eg. "gyawali") and pick table (e.g., "5").
2.  Add item: Just type the food name, price , info and restart the program and the food stored can be found on the end of "menu.txt" file.
3.  Order: Select Option 3. Type "sushi", "burger", and "tea". Type "done" to finish.
4.  Edit: Select Option 4 to remove "tea" if the customer changes their mind.
5.  Move: Select Option 5 to move the customer from Table 5 to Table 1.
6.  Pay: Select Option 6, enter a discount code, and choose "cash" to save the final bill to 'final_bill.txt'.
