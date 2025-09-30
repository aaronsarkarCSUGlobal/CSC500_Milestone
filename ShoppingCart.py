# Module 4: Portfolio Milestone 
# Aaron Sarkar
# September 29th, 2025

# Step 1: Build the ItemToPurchase class
    # Constructor with item_name = "none", item_price=0, item_quantity = 0
    # print_item_cost()

#Initialize class called ItemToPurchase
class ItemToPurchase:
    # Create default constructor for class
        # Initializes item's name = "none", item's price = 0, item's quantity = 0
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name 
        # self.item_name will refer to the 
        # item_name attribute of the ItemToPurchase object
        self.item_price = item_price
        # self.item_price will refer to the 
        # item_price attribute of the ItemToPurchase object
        self.item_quantity = item_quantity
        # self.item_quantity will refer to the 
        # item_quantity attribute of the ItemToPurchase object

    # Creat print_item_cost() function
        # This function multiples the item price by the quantity
        # Example output: Bottled Water 10 @ $1 = $10
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity 
        # calculating total_cost for an item
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

    # Creating a total_cost function 
    def calculate_total_cost(self):
        # returns the total cost for an item
        return self.item_price * self.item_quantity 


# Step 2: Prompt the user for two items and create two objects of the ItemToPurchase class

# First item - user inputs
print("Item 1")
item_one_name = input("Enter the item name:\n") # get item one name from user
item_one_price = float(input("Enter the item price:\n")) # get item one price from user
item_one_quantity = int(input("Enter the item quantity:\n")) # get item one quantity from user
# Create item one object of the ItemToPurchase class
item_one = ItemToPurchase(item_one_name, item_one_price, item_one_quantity)

# Second item - user inputs
print("Item 2")
item_two_name = input("Enter the item name:\n") #get item two name from user
item_two_price = float(input("Enter the item price:\n")) # get item two price from user
item_two_quantity = int(input("Enter the item quantity:\n")) # get item two quantity from user
# Create item two object of the ItemToPurchase class
item_two = ItemToPurchase(item_two_name, item_two_price, item_two_quantity)

# Step 3: Add the costs of the two items together and output the total cost.

# Utilize the calculate_total_cost() function to get the overall cost
total_cost = item_one.calculate_total_cost() + item_two.calculate_total_cost() 
print("\nTOTAL COST")
item_one.print_item_cost() # print item one with print_item_cost()
item_two.print_item_cost() # print item two with print_item_cost()
print(f"Total: ${total_cost:.2f}") # print the total cost