# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# SDH,12.08.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SDH,12.07.2020,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class

    # inserted code from Listing02 here and test code at end to make
    # sure the class worked

    # -- Constructor --
    def __init__(self, product_name='', product_price=""):
        #Attributes
        self.strProdName = product_name
        self.strProdPrice = product_price

    # -- Properties --
    # -- Methods --
# --End of class--

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",")
            row = {"Product": product.strip(), "Price": price.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):

        dicRow = {"Product": strProdPrice, "Price": strProdPrice}
        lstTable.append(dicRow)

        return list_of_rows, 'Success'

    # @staticmethod
    # def write_data_to_file(file_name, list_of_rows):
    #      # renamed objFile to file, strFileName to file_name
    #
    #     file = open(file_name, "w")
    #     for row in list_of_rows:
    #         file.write(row["Product"] + "," + row["Price"] + "\n")
    #     file.close()
    #     print("File has been saved.")
    #
    #     return list_of_rows, 'Success'class Processor:
    # """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Product": product.strip(), "Price": price.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):

        dicRow = {"Product": strProdName, "Price": strPrice}
        lstTable.append(dicRow)

        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # renamed objFile to file, strFileName to file_name

        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Product"] + "," + row["Price"] + "\n")
        file.close()
        print("File has been saved.")

        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass
    # TODO: Add code to show menu to user

    @staticmethod
    def print_menu_Tasks():
        # Display a menu of choices to the user
        print('''
        Menu of Options
        1) Load current data from File
        2) Add new Product Name and Price
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice

    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

while (True):
    # Step 3 Show current data
    # IO.print_current_Tasks_in_list(lstOfProductObjects)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Load current data from File

        Print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)  # read file data
            IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table

            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu


    elif strChoice == '2':  # Add new product name and price


    # elif strChoice == '3':  # Save data to File
    #     strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
    #     if strChoice.lower() == "y":
    #         # TODO: DONE
    #         # code taken from Assign5 (step 4, "save data to file")
    #         # code then moved to the function "write data to file" above
    #         # line written below to then call this function
    #
    #         lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
    #
    #         IO.input_press_to_continue(strStatus)
    #     else:
    #         IO.input_press_to_continue("Save Cancelled!")
    #     continue  # to show the menu

        elif strChoice == '4':  # Exit Program
            print("Goodbye!")
            break  # and Exit





# TESTING
#
# --- Use the class ----
# objP1 = Product()  # with no argument
# objP2 = Product(product_name="Apple", product_price="1000")  # with the parameter and argument
#
# print(objP1.strProdName,)
# objP1.strProdName = "Microsoft"
# objP1.strProdPrice = "800"
# print(objP1.strProdName, objP1.strProdPrice)
# print("-------------")
# print(objP2.strProdName, objP2.strProdPrice)