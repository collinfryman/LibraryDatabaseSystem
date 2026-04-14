"""
Collin Fryman: COP1000
Date: 04/10/2026
Description: This program will allow the City Library to track
book lending, by using lists that act as parallel arrays.
This program will validate every user input and includes a menu,
and a database search function.
"""
#--------INPUT--FUNCTIONS---------------------------------------
def get_fee_rate():
    Input = " "
    fee_rate = " "
    print("Enter daily fee rate (e.g., 0.25): ")
    Input = input()
    while not check_fee_rate(Input):
        print("Invalid input, please try again: ")
        Input = input()
    #END WHILE NOT
    fee_rate = Input
    return fee_rate
#END GET FEE RATE
#---------------------------------------------------------------
def get_search_phone():
    Input = " "
    search_phone = " "
    print("Please enter a phone number to search for: ")
    Input = input()
    while not check_phone(Input):
        print("Invalid input, please try again: ")
        Input = input()
    #END WHILE NOT
    search_phone = Input
    return search_phone
#END GET SEARCH PHONE
#---------------------------------------------------------------
def get_days():
    Input = " "
    days = " "
    print("Enter number of days borrowed: ")
    Input = input()
    while not check_days(Input):
        print("Invalid input, please try again: ")
        Input = input()
    #END WHILE NOT
    days = Input
    return days
#END GET DAYS
#---------------------------------------------------------------
def get_category():
    Input = " "
    category = " "
    print("Enter book category: ")
    Input = input()
    while not check_category_or_title(Input):
        print("Invalid entry, please try again: ")
        Input = input()
    #END WHILE NOT
    category = Input
    return category
#END GET category
#---------------------------------------------------------------
def get_title():
    Input = " "
    title = " "
    print("Enter book title: ")
    Input = input()
    while not check_category_or_title(Input):
        print("Invalid entry, please try again: ")
        Input = input()
    #END WHILE NOT
    title = Input
    return title
#END GET TITLE
#---------------------------------------------------------------
def get_phone():
    Input = " "
    phone = " "
    print("Please enter borrower phone number: ")
    Input = input()
    while not check_phone(Input):
        print("Invalid input. Please try again: ")
        Input = input()
    #END WHILE NOT
    phone = Input
    return phone
#END GET PHONE
#---------------------------------------------------------------
def get_last_name():
    Input = " "
    last_name = " "
    print("Please enter borrower last name: ")
    Input = input()
    while not check_first_or_last_name(Input):
        print("Invalid input. Please try again: ")
        Input = input()
    #END WHILE NOT
    last_name = Input
    return last_name
#END GET LAST NAME
#---------------------------------------------------------------
def get_first_name():
    Input = " "
    first_name = " "
    print("Please enter borrower first name: ")
    Input = input()
    while not check_first_or_last_name(Input):
        print("Invalid input. Please try again: ")
        Input = input()
    #END WHILE NOT
    first_name = Input
    return first_name
#END GET FIRST NAME
#----------DISPLAY--FUNCTIONS-----------------------------------
def display_report(phone, first_name, last_name, title, category, days, fee_rate, fee, count):
    print("-----------------------------------------------------------")
    print("Record #        : ", count + 1)
    print("Phone Number    : ", phone[count])
    print("Borrower Name   : ", first_name[count]," ", last_name[count])
    print("Book Title      : ", title[count])
    print("Category        : ", category[count])
    print("Days Borrowed   : ", days[count])
    print("Daily Fee Rate  : ", fee_rate[count])
    print("Total Late Fee  : ", fee[count])
    print("-----------------------------------------------------------")
#END DISPLAY REPORT
#---------------------------------------------------------------
def display_all(phone, first_name, last_name, title, category, days, fee_rate, fee, count):
    i = 0
    while i < count:
        display_report(phone, first_name, last_name, title, category, days, fee_rate, fee, i)
        i = i + 1
    #END WHILE i
#END DISPLAY ALL
#---------------------------------------------------------------
def display_stats(fee, count):
    total_fee = 0.00
    average_fee = 0.00
    i = 0
    while i < count:
        total_fee = total_fee + fee[i]
        i = i + 1
    #END WHILE i
    if count > 0:
        average_fee = round(total_fee / count, 2)
    else:
        average_fee = 0.00
    #END IF....ELSE
    print("-----------------------------------------------")
    print("Total Records     : ", count)
    print("Total Late Fees   : ", round(total_fee, 2))
    print("Average Late Fee  : ", average_fee)
    print("-----------------------------------------------")
#---------------------------------------------------------------
def search_record(phone, search_phone, count):
    i = 0
    while i < count:
        if search_phone == phone[i]:
            return i
        else:
            i = i + 1
        #END IF...ELSE
    #END WHILE i
    return -1
#END SEARCH RECORD
#-------------CALCULATION--FUNCTIONS----------------------------
def calc_fee(days, fee_rate):
    fee = 00
    fee = round(float(days) * float(fee_rate), 2)
    return fee
#END CALC FEE
#---------VALIDATION--FUNCTIONS---------------------------------
def check_fee_rate(Input):
    i = 0
    dot_count = 0
    if len(Input) == 0:
        return False
    #END IF EMPTY
    while i < len(Input):
        if not Input[i].isdigit() and Input[i] != ".":
            return False
        #END IF NOT DOT OR DIGIT
        if Input[i] == ".":
            dot_count = dot_count + 1
        #END IF DOT
        if dot_count > 1:
            return False
        #END IF TOO MANY DOTS
        i = i + 1
    #END WHILE i
    if float(Input) <= 0:
        return False
    #END IF NOT ABOVE ZERO
    return True
#END CHECK FEE RATE
#---------------------------------------------------------------
def check_category_or_title(Input):
    if len(Input) > 0:
        return True
    #END LEN GREATER THAN ZERO
#END CHECK CATEGORY
#---------------------------------------------------------------
def check_days(Input):
    i = 0
    if len(Input) <= 0:
        return False
    #END IF NO INPUT
    while i < len(Input):
        if not Input[i].isdigit():
            return False
        #END IF NOT DIGIT
        else:
            i = i + 1
        #END ELSE
    #END WHILE i
    if int(Input) <= 0:
        return False
    #END IF LESS THAN OR EQUAL TO ZERO
    return True
#END CHECK DAYS
#---------------------------------------------------------------
def check_phone(Input):
    i = 0
    if len(Input) != 10:
        return False
    #END IF NOT 10 DIGITS
    while i < len(Input):
        if not Input[i].isdigit():
            return False
        else:
            i = i + 1
        #END IF...ELSE NOT DIGIT
    #END WHILE i
    return True
#END CHECK PHONE
#---------------------------------------------------------------
def check_selection(Input):
    if Input != "1" and Input != "2" and Input != "3" and Input != "4":
        return False
    #END IF NOT VALID
    return True
#END CHECK SELECTION
#---------------------------------------------------------------
def check_first_or_last_name(Input):
    i = 0
    if len(Input) == 0:
        return False
    #END IF EMPTY
    while i < len(Input):
        if not Input[i].isalpha():
            return False
        else:
            i = i + 1
        #END IF..ELSE
    #END WHILE i
    return True
#END CHECK first name
#---------------------------------------------------------------
def main_menu():
    selection = 0
    Input = " "
    print("----------------------------------")
    print("Welcome to the City Library System")
    print("----------------------------------")
    print("-----------Main Menu--------------")
    print("1. Add a borrowing record")
    print("2. Display all records")
    print("3. Search for a record")
    print("4. Quit program")
    Input = input()
    while not check_selection(Input):
        print("Invalid entry. Please try again: ")
        Input = input()
    #END WHILE NOT
    selection = int(Input)
    return selection
#END MAIN MENU
#---------------------------------------------------------------
def main():
    #DECLARATIONS, ARRAYS
    phone      = 100 * [" "]
    first_name = 100 * [" "]
    last_name  = 100 * [" "]
    title      = 100 * [" "]
    category   = 100 * [" "]
    days       = 100 * [000]
    fee_rate   = 100 * [0.00]
    fee        = 100 * [0.00]
    #WORKING VARIABLES
    count        = 0 #KEEPS COUNT OF HOW MANY RECORDS ARE STORED
    selection    = 0
    found_at     = -1
    search_phone = " "
    #DISPLAY MAIN MENU
    selection = main_menu()
    #INPUTS AND VALIDATIONS
    while selection != 4:
        if selection == 1:
            if count == 100:
                print("The City Library System is at full capacity: Cannot add more records.")
                selection = main_menu()
            #END IF SYSTEM IS FULL
            else:
                phone[count] = get_phone()
                first_name[count] = get_first_name()
                last_name[count] = get_last_name()
                title[count] = get_title()
                category[count] = get_category()
                days[count] = get_days()
                fee_rate[count] = get_fee_rate()
                #CALCULATE FEE
                fee[count] = calc_fee(days[count], fee_rate[count])
                #DISPLAY THE USERS INPUTS
                display_report(phone, first_name, last_name, title, category, days, fee_rate, fee, count) 
                count = count + 1
                print("Press any key to return to the Main Menu: ")
                input()
                selection = main_menu()
            #END IF...ELSE 1
        #END IF SELECTION == 1
        else:
            if selection == 2:
               if count != 0:
                   #DISPLAY ALL EMPLOYEES
                   display_all(phone, first_name, last_name, title, category, days, fee_rate, fee, count)
                   print("Press any key to return to the Main Menu: ")
                   input()
                   selection = main_menu()
               else:
                   print("No records found, please add a record first")
                   selection = main_menu()
            else:
                if selection == 3:
                    if count != 0:
                        #SEARCH FOR A RECORD
                        search_phone = get_search_phone()
                        found_at = search_record(phone, search_phone, count)
                        if found_at == -1:
                            print(search_phone, "Could not be found.")
                            selection = main_menu()
                        else:
                            display_report(phone, first_name, last_name, title, category, days, fee_rate, fee, found_at)
                            print("Press any key to return to the Main Menu: ")
                            input()
                            selection = main_menu()
                        #END IF...ELSE FOUND_at
                    else:
                        print("No records found, please add a record first: ")
                        selection = main_menu()
                    #END IF...ELSE... COUNT
                else:
                    print("Invalid input, please try again: ")
                #END IF...ELSE
            #END IF....ELSE
        #END IF...ELSE
    #END WHILE NOT DONE
    display_stats(fee, count)
    print("Goodbye!")
#END MAIN       
#---------------------------------------------------------------
main()
#---------------------------------------------------------------
