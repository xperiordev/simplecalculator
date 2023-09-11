print("PyCalculator")
print("Made with hand by XperiorDev.")

print("********** MAIN MENU **********")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("*******************************")

option = int(input("Choose for operator ( 1 - 5 ) : "))

if option < 1 and option > 5:
    print("Error! Please try again to run the program.")
else:
    firstNumber = int(input("Enter for first number : "))
    secondNumber = int(input("Enter for second number : "))

    if option == 1:
        operator = "+"
        result = firstNumber + secondNumber
    elif option == 2:
        operator = "-"
        result = firstNumber - secondNumber
    elif option == 3:
        operator = "*"
        result = firstNumber * secondNumber
    elif option == 4:
        operator = "/"
        result = firstNumber / secondNumber
    elif option == 5:
        operator = "%"
        result = firstNumber % secondNumber
    else:
        print("Error! Please try again to run the program.")

    print("***** Result *****")
    print(firstNumber, operator, secondNumber, "=", result)
