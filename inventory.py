# Import relevant libraries
from tabulate import tabulate

#========The beginning of the class==========
class Shoe():
    '''A simulation of shoes in the warehouse.'''

    def __init__(self, country, code, product, cost, quantity):
        # Initialize class attributes.

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''This method returns the cost of the shoe.'''

        return self.cost

    def get_quantity(self):
        '''This method returns the quantity of the shoes.'''

        return self.quantity

    def __str__(self):
        '''This method returns a string representation of a class.'''
 
        shoe_descr = [self.country, self.code, self.product, self.cost, self.quantity]

        return shoe_descr

    def update_stock(self, qty):
        '''This method updates the quantity of a product'''

        self.quantity = str(int(self.quantity) + qty)


shoe_list = []    # The list will be used to store a list of shoe objects.


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list.
    '''

    fhand = None
    try:
        fhand = open("inventory.txt", "r")
        content = fhand.readlines()[1:]
        for line in content:
            line = line.rstrip()
            line = line.split(",")
            shoe_obj = Shoe(line[0], line[1], line[2], line[3], line[4])
            shoe_list.append(shoe_obj)
            
    except FileNotFoundError:
        print("The inventory file does not exist. Add the file and try again")
    finally:
        if fhand is not None:
            fhand.close()


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    country = input("Enter the country: ").title()
    code = input("Enter product code: ").upper()
    product = input("Enter product name: ").title()
    cost = input("Enter product cost: ")
    quantity = input("Enter the product quantity: ")

    new_shoe_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe_object)

    # Write new shoe object in the inventory file
    try:
        fhand = open("inventory.txt", "a")
        fhand.write(country + "," + code + "," + product + "," + cost + "," + quantity + "\n")
        fhand.close
    except FileNotFoundError:
        print("The inventory file does not exist. Add the file and try again")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''

    outer_list = [] # Initialize list to hold shoe object descriptions
    headings = ["Country", "Code", "Product", "Cost", "Quantity"] # Initialize headers for table 
    for shoe in shoe_list:
        outer_list.append(shoe.__str__())

    print(tabulate(outer_list, headings))


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    # Call read_shoes_data to create shoe object and create list
    shoe_list = []
    read_shoes_data()

    # Get the shoe object with the lowest quantity
    # The quantites are stored in a list and the index of the minimum is found 
    qty_list = []
    for shoe_obj in shoe_list:
        qty_list.append(int(shoe_obj.quantity))
    idx_of_min = qty_list.index(min(qty_list))
    print("The following product has the lowest quantity:\n{}, {}, {}, {}, {}"\
    .format(shoe_list[idx_of_min].country, \
            shoe_list[idx_of_min].code, \
            shoe_list[idx_of_min].product, \
            shoe_list[idx_of_min].cost, \
            shoe_list[idx_of_min].quantity))

    while True:
        option = input('''\nSelect one of the following options below:
        # yes - Stock up on this product
        # no - Go back to main menu
        # : ''').casefold()

        if option == "yes":
            while True:
                num_shoes_to_add = input("Enter the quantity to add: ")
                try:
                    shoe_list[idx_of_min].update_stock(int(num_shoes_to_add))
                    break
                except:
                    num_shoes_to_add = -1
                
                if num_shoes_to_add == -1:
                    print("Invalid number entered")
                
            # Update changes to quantity in the inventory file
            try:
                file_h = open("inventory.txt", "r")
                list_of_lines = file_h.readlines()[1:]
                new_line = list_of_lines[idx_of_min].split(",")
                new_line[-1] = shoe_list[idx_of_min].get_quantity() + "\n"
                new_line = ",".join(new_line)
                list_of_lines[idx_of_min] = new_line
                file_h = open("r.txt", "w")
                file_h.writelines(list_of_lines)
                file_h.close()

            except FileNotFoundError:
                    print("The inventory file does not exist. Add the file and try again")
                    break

        elif option == "no":
            break

        else:
            print("Invalid option selected")


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # Call read_shoes_data to create shoe object and create list
    shoe_list = []
    read_shoes_data()

    shoe_code = input("Enter the product code: ").upper()
    print("searching in database...")
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            outer_list = [] # Initialize list to hold shoe object description
            headings = ["Country", "Code", "Product", "Cost", "Quantity"] # Initialize headers for table
            outer_list.append(shoe.__str__())
            print(tabulate(outer_list, headings))

            break


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Call read_shoes_data to create shoe object and create list.
    shoe_list = []
    outer_list = [] # Initialize list to hold shoe object descriptions to be tabulated
    headings = ["Product", "Code", "Value"]
    read_shoes_data()

    for shoe in shoe_list:
        value_map = []
        value_map.append(shoe.product)
        value_map.append(shoe.code)
        stock_value = round((int(shoe.cost) * int(shoe.quantity)),2)
        value_map.append(str(stock_value))
        outer_list.append(value_map)

    print(tabulate(outer_list, headings))


def highest_qty():
    '''
    This function determines the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Call read_shoes_data to create shoe object and create list
    shoe_list = []
    read_shoes_data()

    # Get the shoe object with the highest quantity
    # The quantites are stored in a list and the index of the maximum is found 
    qty_list = []
    for shoe_obj in shoe_list:
        qty_list.append(int(shoe_obj.quantity))
    idx_of_max = qty_list.index(max(qty_list))
    print("The following product is for sale:\n{}, {}, {}, {}, {}"\
    .format(shoe_list[idx_of_max].country, \
            shoe_list[idx_of_max].code, \
            shoe_list[idx_of_max].product, \
            shoe_list[idx_of_max].cost, \
            shoe_list[idx_of_max].quantity))

#==========Main Menu=============
while True:
    # presenting the menu to the user.
    menu = input('''Select one of the following options from the menu below:
r - Read shoes data
cs - Capture new shoes data
va - View all shoes
rs - Re-stock shoes
ss - Search for shoes
gv - Get stock value of each product
hq - Get the highest quantity to be marked for sale
e - Exit
: ''').casefold()

    if menu == "r":
        read_shoes_data()

    elif menu == "cs":
        capture_shoes()

    elif menu == "va":
        view_all()

    elif menu == "rs":
        re_stock()

    elif menu == "ss":
        search_shoe()

    elif menu == "gv":
        value_per_item()

    elif menu == "e":
        exit()

    else:
        print("Invalid option")