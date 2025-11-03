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
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description="none"):
        self.item_name = item_name 
        # self.item_name will refer to the 
        # item_name attribute of the ItemToPurchase object
        self.item_price = item_price
        # self.item_price will refer to the 
        # item_price attribute of the ItemToPurchase object
        self.item_quantity = item_quantity
        # self.item_quantity will refer to the 
        # item_quantity attribute of the ItemToPurchase object
        self.item_description = item_description
        # self.item_descriptions will refer to the 
        # item_description attrivute of the ItemToPruchse object

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

# Note: steps 2 & 3 have been commented out but not removed. I wanted to include them still, but
# the menu should handle adding and removing items from the shopping cart
# Step 2: Prompt the user for two items and create two objects of the ItemToPurchase class
'''
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
'''

# Module 6: Portfolio Milestone 
# Step 4: 
# Build the Shoppinng Cart Class with the following
    # Constructor customer_name = "none", current_date = "January 1, 2020", cart_items = []
    # add_item()
    # remove_item()
    # modify_item()
    # get_num_items_in_cart()
    # get_cost_of_cart()
    # print_total()
    # print descriptions()

# Initialize Class called Shopping Cart
class ShoppingCart:
    # create constructor with parameters from above
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name 
        # self.customer_name will refer to customer_name in the ShoppingCart class
        self.current_date = current_date
        # self.current_date will refer to current_date in the ShoppingCart class
        self.cart_items = []
        # self.cart_items will refer to a list in the shoppingcart class

    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything
    def add_item(self, item):
        self.cart_items.append(item) # add new item to cart_items list

    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name):
        # create a boolean to use as a flag to check if item exists
        item_exists = False
        # loop through items in cart
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_exists = True
                break
        if item_exists == False:
            print("Item not found in cart. Nothing removed.")

    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    # If item can be found (by name) in cart, check if parameter has default values for description, price, and 
    # quantity. If not, modify item in cart.
    # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, modified_item): # modified item is the item name we are looking for
        # create a boolean to use as a flag to check if item exists
        item_exists = False
        #loop through the cart items
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                # item was found switch the boolean to TRUE
                item_exists = True
                # change the price if its not missing
                if modified_item.item_price != 0: # make sure modified item price isn't null
                    item.item_price = modified_item.item_price # change old price to new price
                # modify the quanity
                if modified_item.item_quantity != 0: # make sure modified item quantity isn't null
                    item.item_quantity = modified_item.item_quantity # modify quantity
                # change the description
                if modified_item.item_description != "none": # make sure description isn't null
                    item.item_description = modified_item.item_description # update description
                break
        # if the item was never found 
        if item_exists == False:
            print("Item not found in cart. Nothing modified")        

    # Returns quantity of all items in cart. Has no parameters
    def get_num_items_in_cart(self):
        # create varaible to store total items
        total_items = 0
        # loops through all items 
        for item in self.cart_items:
            total_items += item.item_quantity # increment count based on quantity per item       
        return total_items # return the total amount of items

    # determines and returns the total cost of items in cart. Has no parameters
    def get_cost_of_cart(self):
        # create varaible to store total items
        total_cost = 0
        # loops through all items 
        for item in self.cart_items:
            total_cost += item.calculate_total_cost() # increment count based on cost per item  
        return total_cost # return the total cost of all items
    
    # Outputs total of objects in cart. 
    # If the cart is empty print "SHOPPING CART IS EMPTY"
    def print_total(self):
        # print name of user and the date
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        # check if the cart is empty first
        if len(self.cart_items) == 0: # check if length of cart list is zero
            print("SHOPPING CART IS EMPTY")
        else:
            # print the number of items by using the get number of items function 
            print(f"Number of Items: {self.get_num_items_in_cart()}") 
            # loop through all the items 
            for item in self.cart_items:
                # print item cost by using print_item_cost()
                item.print_item_cost()
            # print the total cost of the shopping cart
            print(f"Total: ${self.get_cost_of_cart():.2f}") # print with 2 decimals only

    # Output each item's description
    def print_descriptions(self):
        # print name of user and the date
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions") # from example output
        # Loop through all items
        for item in self.cart_items:
            # print the item name and its description
            # Note: I had to add item_desciption to the ItemToPurchase constructor
            print(f"{item.item_name}: {item.item_description}")

# Step 5 & 6:
# implement the print_menu() function. Call print_menu() in the main() function
 # MENU
    # a - Add item to cart
    # r - Remove item from cart
    # c - Change item quantity
    # i - Output items' descriptions
    # o - Output shopping cart
    # q - Quit
    # Choose an option:
# Implement output shopping cart menu option

# create print_menu function
def print_menu(cart):
    # Create a option string
    option = ""
    # options menu remains open until "q"(quit) is entered
    while option != "q":
        # print the example menu provided 
        print("\nMENU") 
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        # get the option from the user
        option = input("Choose an option:\n")

        # check if the option selected is in the list
        while option not in ['a', 'r', 'c', 'i', 'o', 'q']:
            # option was invalid so tell user to pick a new one
            option = input("Choose a valid option: \n")
        
        # Step 7, 8 & 9
        # Implement add item to cart menu option
        # Implement remove item menu option
        # Implement change item quantity menu option 
        # option to add item to cart
        if option == 'a':
            print("ADD ITEM TO CART") # print statement from instructions
            name = input("Enter the item name:\n") # ask user to enter the items name
            description = input("Enter the item description:\n") # ask user to enter the items description
            price = float(input("Enter the item price:\n")) # ask user to enter the items price
            quantity = int(input("Enter the item quantity:\n")) # ask user to enter the items quantity
            item = ItemToPurchase(name, price, quantity, description) # create an instance with the user inputs
            cart.add_item(item) # add the new item to the cart
            print("Item added to cart!") # print to let the user know item added to cart       
        
        # option to remove item from cart
        elif option == 'r': # option was r
            print("REMOVE ITEM FROM CART") # print statement from instructions
            name = input("Enter name of item to remove:\n") # ask the user for the name of the item
            cart.remove_item(name) # remove the item from the cart
        
        # option to change item quantity
        elif option == 'c': # option was c
            print("CHANGE ITEM QUANTITY")
            name = input("Enter name of item:\n") # ask the user for the name of the item
            quantity = int(input("Enter the new item quantity:\n")) # ask user to enter the new items quantity
            modified_item = ItemToPurchase(item_name=name, item_quantity=quantity) # create new instance with new quantity
            cart.modify_item(modified_item) # call modify item function to modify the cart item's quantity
        
        # output item descriptions
        elif option == "i": # option was i
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        
        # output shopping cart
        elif option == "o": # option was o
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        
        # quit
        elif option == "q":
            # if option is quit the menu
            break
        
# simple main section to test the functionality of my code
if __name__ == "__main__":
    # ask user for two inputs: name and date
    # Ask the user for customer for name and today's date
    customer_name = input("Enter customer's name: \n") #input for customer's name
    current_date = input("Enter the current date: \n") # input for current date 
    print(f"\nCustomers name: {customer_name}")
    print(f"\nToday's date: {current_date}")

    # create a shopping cart with user name and date
    cart = ShoppingCart(customer_name, current_date) # Object created for Step 7

    # test the menu 
    print_menu(cart)


