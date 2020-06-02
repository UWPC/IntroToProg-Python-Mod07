# -------------------------------------------------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Exception Handling using try-except block.
#              Catching Specific Exceptions.
# ChangeLog (Who,When,What):
# PCoonrad,5.29.2020,Created script
# PCoonrad,5.31.2020,Modified code: Added ValueError exception
# -------------------------------------------------------------------------------------------------------------------- #

# Exception Handling using try-except block ----------------------------------#

# Data ---------------------------------------------------------------------- #
strNum1 = ""  # Captures the user input value
strNum2 = ""  # Captures the user input value
intDiv = ""  # Captures the division value
e = ""  #
# Presentation (Input/Output)  ---------------------------------------------- #
while(True):  # loop so user can input new data if exception occurs
    strNum1 = input("\nEnter a first number: ")
    strNum2 = input("Enter a second number: ")

# Processing  --------------------------------------------------------------- #
#try/except/else
    try:  # section code that can raise exception
        fltDiv = float(strNum1) / float(strNum2)
    # except clauses with block of statements that run when exception is raised
    except ValueError:  # argument has the right type but inappropriate value
        print('Invalid character. Please enter a number.')  # custom message for the built-in exception
    except ZeroDivisionError:  # second argument of a division is zero
        print('Divisor cannot equal zero. Please enter a valid divisor.')  # custom message for the built-in exception
    except Exception as e:  # exception class at the bottom will catch any other non-specific type of error
        print('Something went wrong.')  # custom message for the built-in exception
        print("Python Built-In error message:", (e))  # custom message with Python messages for the built-in exception
    # else block executes if no exception is raised in try block
    else:
        print('The quotient of ' + strNum1 + ' and ' + strNum2 + ' is: ' + str(fltDiv))
        break # stops loop when no exception occurs

input("\nPress the 'Enter' key to exit.")

