
#Function for heating & Cooling

print("$" *50)
print('Welcome to Heating Cooling Function'.upper())
print("$" *50)
option = 'y'
#function to check actaul and desire temprature and print reuslt accordingly
def HeatingCooloing(actualTemp,desiredTemp) :
        if actualTemp > desiredTemp:
            print("\t\nTurn on cooling system.")
        elif actualTemp < desiredTemp:
            print("\t\nTurn on heating system.")
        else:
            print("\t\nstandby.")
#Function to to take celsius value and convert into unit as per user's need
def Conversion(tempCelsius,targetUnit):
    # # Check the target unit and log the converted temperature
    if targetUnit == 'F':
        tempCelsius = tempCelsius * 9 / 5 + 32 # formula to convert value into Fahrenheit
        print('\t\nTemperature in  Fahrenheit  is {}'.format(tempCelsius))
    elif targetUnit == 'K':
        print('\t\nTemperature in Kelvin is {}'.format(tempCelsius))
        tempCelsius: tempCelsius + 273.15 # formula to convert value into kelvin
    else:
        print('\t\nTemperature in Celsius is {}'.format(tempCelsius))


# while loop to control execution of code until conditions are met
while True:
    while True: # while loop to accept valid  actual  temperature from user
        try:        #try catch loop to throw error
            actualTemp = int(input("\t\nPlease enter actual temp"))
            break
        except ValueError:
            print("\t\noops! That was not a valid integer.Please try again...")
            continue

    while True: # while loop to accept valid desire temperature from user
        try:
             desiredTemp = int(input("\t\nPlease enter desire temp "))
             break  # break out of the inner while loop if user provided number is integer
        except ValueError:
            print("oops! That was not a valid integer.Please try again...")
            continue
    HeatingCooloing(actualTemp, desiredTemp)    #function call to print heating cooling function in the main program
    # while loop to accept valid  temperature in Celsius  from user
    while True:
        try:
            tempCelsius =int(input('\t\nPlease enter temperature in Celsius'))
            break
        except ValueError:
            print("\t\nOops! That was not a valid integer.Please try again...")
            continue
    #while loop to accept valid  targetunit data from user
    while True:
            targetUnit  = input('Enter target Unit F for  Fahrenheit  K for Kelvin and C for Celsius')
            targetUnit = targetUnit.upper()
            if targetUnit == 'F':
                Conversion(tempCelsius, targetUnit)
                break
            elif targetUnit == 'K':
                Conversion(tempCelsius, targetUnit)
                break
            elif targetUnit == 'C':
                Conversion(tempCelsius, targetUnit)
                break
            elif not targetUnit.isalpha() or len(targetUnit) != '1' or not targetUnit.startswith('K') or not targetUnit.startswith('F') or not targetUnit.startswith('C'):
                print("\t\nOops! That was not a valid choice , please enter F ,K or C.. try again...")
                continue
            else:
                break
     #While Loop to check valid choice to either exit or continue code execution
    while True:
        choice = input('\t\n\tWould like to continue(y/n)')
        if choice == 'y':
            print("Continue...")
            break
        elif choice == 'n':
            print("Thanks...")
            exit()
        else:
            print("Please enter valid choice...")
            continue

