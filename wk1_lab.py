"""Angelo Barcelona SDEV300; voter registration"""
import sys

MIN_AGE = 18
MAX_AGE = 115
GOODBYE_MESSAGE = "GOODBYE"
STATE_LIST = {}

#OPENS THE FILES STATE.TXT AND LOADS THE LIST OF STATES IN TO A DICT.
with open("states.txt", encoding="utf-8") as f:
    STATE_LIST = dict(x.rstrip().split(None, 1) for x in f)


def registered_messege(age, citizenship, first_name, last_name, state_of_residence, zipcode):
    """Prints the final message to the user after all data has been collected"""
    print("**********************************************************************************")
    print("* Thank you for registering to vote below is the information received.")
    print("* Please check that the information is correct, if it is type F to finish or")
    print("* type N if the information is not correct and you will be prompted to start")
    print("* again.")
    print(f"* Age: {age}")
    print(f"* First Name: {first_name}")
    print(f"* Last Name: {last_name}")
    print(f"* United States Citizen: {citizenship}")
    print(f"* State of Residence: {state_of_residence}")
    print(f"* Zipcode: {zipcode}")
    print("**********************************************************************************")
    finished = input("Is this information correct? Type F to finish, "
                     "E to exit, or R to restart: ").upper()
    return finished


def get_zipcode():
    """get_zipcode method allows us to get the users zipcode for further use and storage"""
    while True:
        zipcode = input("Please enter your 5 digit zipcode or enter e to exit: ")
        if zipcode == "e":
            goodbye()
        if len(zipcode) != 5 or not zipcode.isdigit():
            print("Invalid zipcode.  Please try again")
        else:
            break
    return zipcode


def state_of_residence():
    """This method gets the state of residence as a two letter
    abbreviation and returns it to be read by STATE_LIST"""
    condition = True
    while condition:
        residence = input("Please type the two letter abbreviation for your state of residence or"
                          " type e to exit: ").upper()
        if residence == "e":
            goodbye()
        if len(residence) != 2 or residence.isdigit():
            print("Not a valid state. Please try again.")
        else:
            for values in STATE_LIST.values():
                if values == residence.upper():
                    condition = False

    return residence


def citizenship():
    """this method is used to determine if the applicant is a U.S. citizen or not"""
    while True:
        us_citizen = input("Are you a United States Citizen?"
                           " Type Y(yes)/N(no) or e to exit: ").upper()
        if us_citizen in {"Y", "N", "E"}:
            break
        print("Not a valid response.  Please try again")
    if us_citizen == "E":
        goodbye()
    if us_citizen == "N":
        print("Sorry but you must be a United States Citizen to register to vote.")
        goodbye()
    return us_citizen


def goodbye():
    """This method is used to tell the user goodbye if they exit the program before completion"""
    print(GOODBYE_MESSAGE)
    sys.exit()


def welcome():
    """welcome message the user will answer Y or N, if Y they will continue else they will exit"""
    while True:
        user_welcome = input("Welcome to the voter registration application,"
                             " would you like to register?  Y/N: ").upper()
        if user_welcome.strip() == '':
            print("Not a valid response.  Please try again.")
        if user_welcome == "N":
            goodbye()
        elif user_welcome == "Y":
            break
    return user_welcome


def get_first_name():
    """Gets the name of the user or allows them to terminate the application"""
    while True:
        first_name = input("Please type your first name to continue or e to exit: ")
        if first_name == "e":
            goodbye()
        elif first_name.strip() == '' or len(first_name) < 2:
            print("Not a valid Name.")
        else:
            return first_name


def get_last_name():
    """Gets the name of the user or allows them to terminate the application"""
    while True:
        last_name = input("Please type your last name to continue or e to exit: ")
        if last_name == "e":
            goodbye()
        elif last_name.strip() == '' or len(last_name) < 2:
            print("Not a valid Name.")
        else:
            return last_name


def get_age():
    """Gets users age or allows them to terminate the application"""
    while True:
        age = input("Please type your age or type e to exit: ")
        if age == "e":
            goodbye()
        if age.isdigit():
            age = int(age)
            if MIN_AGE <= age <= MAX_AGE:
                return age
            print("Age not valid to register to vote")
        else:
            print(f"The {age} is not a valid age.")

    return None


def main():
    """Main function that the program runs from, all functions will be called here"""

    if welcome():
        age = get_age()
        print()
        us_citizen = citizenship()
        print()
        first_name = get_first_name()
        print()
        last_name = get_last_name()
        print()
        state_of_res = state_of_residence()
        print()
        zipcode = get_zipcode()
        print()
        complete = registered_messege(age, us_citizen, first_name, last_name, state_of_res, zipcode)
        if complete == "R":
            main()
        elif complete == "F":
            print("Your registration card should arrive in the mail in 2 weeks.")
            goodbye()
        else:
            goodbye()


main()
