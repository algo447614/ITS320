#------------------------------------------------------------------------
# Program Name: ITS320_CTA2_Option1
# Author: Aliciana Gondick
# Date: Aug. 27, 2023
#------------------------------------------------------------------------
# Pseudocode:   1. Program will allow for user to input string
#               2. Program will evaluate string for 5 data types
#               3. Program will produce "True" or "False" for each data type evaluated, with "True" representing the data type found
#------------------------------------------------------------------------
# Program Inputs: String 'S'
# Program Outputs: Displays True or False values for 5 data verification types, all on a separate line
#------------------------------------------------------------------------
print("This program will verify the data types of user input")
S=input("type here: ")

print("String is alphanumeric: ",S.isalnum())

print("String is all alphabetical: ",S.isalpha())

print("String is all digits: ",S.isdigit())

print("String is all lowercase: ",S.islower())

print("String is all uppercase: ",S.isupper())

print("Thank you for using this program")
