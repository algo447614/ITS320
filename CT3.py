#------------------------------------------------------------------------
# Program Name: ITS320_CTA3_Option1
# Author: Aliciana Gondick
# Date: Aug. 31, 2023
#------------------------------------------------------------------------
# Pseudocode:
#   1 . Input vehicle year for Ferrari 250 GTO
#   2. Validate year by checking that it is a number between 1962 and 2014
#   3. Return value corresponding to year of vehicle
#       a. 1962 - 1964: 18500
#       b. 1965 - 1968: 6000
#       c. 1969 - 1971: 12000
#       d. 1972 - 1975: 48000
#       e. 1976 - 1980: 200000
#       f. 1981 - 1985: 650000
#       g. 1986 - 2012: 35000000
#       h. 2013 - 2014: 52000000
#------------------------------------------------------------------------
# Program inputs: Year of vehicle (Ferrari 250 GTO)
# Program Outputs: Return value of vehicle in USD ($)
#------------------------------------------------------------------------


print("Ferrari 250 GTO value by year")
Year = 0
Value = 0
InputValue = ""

InputValue = input("Please enter year:")

if InputValue == " ":
    print("No year provided")
else:
        if not (InputValue.isdigit()):
            print("Please enter a valid year")
        else:
            Year = int(InputValue)
            if (Year < 1962) or (Year > 2014):
                print("No value: Ferrari 250 GTO was made from 1962 to 2014")

if 1962 <= Year <= 1964:
    Value = 18500
elif 1965 <= Year <= 1968:
    Value = 6000
elif 1969 <= Year <= 1971:
    Value = 12000
elif 1972 <= Year <= 1975:
    Value = 48000
elif 1976 <= Year <= 1980:
    Value = 200000
elif 1981 <= Year <= 1985:
    Value = 650000
elif 1986 <= Year <= 2012:
    Value = 35000000
elif 2013 <= Year <= 2014:
    Value = 52000000


print("${:,.2f}".format(Value))

print("Thank you for using this program")
