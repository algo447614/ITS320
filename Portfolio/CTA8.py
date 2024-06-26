#------------------------------------------------------------------------
# Program Name: ITS320_CTA8_OPTION1_PORTFOLIO
# Author: Aliciana Gondick
# Date: Oct. 08, 2023
#------------------------------------------------------------------------
# Pseudocode:
#  Program will present a menu of options for purpose of managing
# vehicle inventory. Program will allow user to add inventory, update, delete,
# view, and export inventory. 
#------------------------------------------------------------------------
# Program inputs: Menu options, vehicle inventory 
# Program Outputs: Inventory list and manipulation, export to a text file
#------------------------------------------------------------------------
print('Vehicle Inventory')
class Automobile:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._mileage = 0
        self._price = 0
        
    def addVehicle(self):
        try:
            self._make = input('Enter vehicle make: ')
            self._model = input('Enter vehicle model: ')
            self._year = int(input('Enter vehicle year: '))
            self._color = input('Enter vehicle color: ')
            self._mileage = int(input('Enter vehicle mileage: '))
            self._price = int(input('Enter vehicle price: '))
            return True
        except ValueError:
            print('Invalid input: Only whole numbers are accepted.')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._year, self._color, self._mileage, self._price])


class Inventory:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self):
        vehicle = Automobile()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print ()
            print('This vehicle has been added')
    def viewInventory(self):
        print('\t'.join(['','Make', 'Model','Year', 'Color', 'Mileage', 'Price']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx + 1, end='\t')
            print(vehicle)


inventory = Inventory()
while True:
    print('#1 Add Vehicle to Inventory')
    print('#2 Delete Vehicle from Inventory')
    print('#3 View Current Inventory')
    print('#4 Update Vehicle Inventory')
    print('#5 Export Current Inventory')
    print('#6 Quit')
    userInput = input('Please choose from the menu: ')
    if userInput == '1':
        inventory.addVehicle()
    elif userInput == '2':
        if len(inventory.vehicles) < 1:
            print('No vehicles in inventory')
            continue
        inventory.viewInventory()
        item = int(input('Enter the inventory number of the vehicle you would like to remove: '))
        if item - 1 > len(inventory.vehicles):
            print('Invalid number')
        else:
            inventory.vehicles.remove(inventory.vehicles[item - 1])
            print()
            print('Vehicle removed')
    elif userInput == '3':
        if len(inventory.vehicles) < 1:
            print('No vehicles in inventory')
            continue
        inventory.viewInventory()
    elif userInput == '4':
        if len(inventory.vehicles) < 1:
            print('No vehicles in inventory')
            continue
        inventory.viewInventory()
        item = int(input('Enter the inventory number of the vehicle you would like to update: '))
        if item - 1 > len(inventory.vehicles):
            print('Invalid number')
        else:
            automobile = Automobile()
            if automobile.addVehicle() == True:
                inventory.vehicles.remove(inventory.vehicles[item - 1])
                inventory.vehicles.insert(item - 1, automobile)
                print()
                print('Vehicle updated')
    elif userInput == '5':
        if len(inventory.vehicles) < 1:
            print('No vehicles in inventory')
            continue
        f = open('vehicle_inventory.txt', 'w')
        f.write('\t'.join(['Make', 'Model','Year', 'Color', 'Mileage', 'Price']))
        f.write('\n')
        for vehicle in inventory.vehicles:
            f.write('%s\n' %vehicle)
        f.close()
        print('The vehicle inventory has been exported to a text file')
    elif userInput == '6':
        print('Goodbye')
        break
    else:
        print('Invalid input. Try again.')
