# ------------------------------------------------- #
# Title: Pickling and Unpickling
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# PCoonrad,5.30.2020,Created Script
# PCoonrad,5.31.2020,Updated Script: Processing layer
# PCoonrad,6.01.2020,Updated Script: Presentation layer
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []  # List from user input
intId = ""  # Captures the user input value
strName = ""  # Captures the user input value

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, 'wb')
    pickle.dump(list_of_data, objFile)  # store data using the pickle dump method
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    objFileData = pickle.load(objFile)
    objFile.close()
    return objFile

# Presentation ------------------------------------ #
intId = int(input("Enter an Id: "))  # request input from user
strName = str(input("Enter a Name: "))  # request input from user
list_of_data = [intId, strName]
save_data_to_file(strFileName, list_of_data)
print(read_data_from_file(file_name=strFileName))

input("\nPress the 'Enter' key to exit.")
