print("Hello, Please Select an Option")
print("Option 1: Fahrenheit to Celsius")
print("Option 2: Celsius to Fahrenheit")
choice = input("Please select Option 1 or Option 2")
if choice == "Option 1" or choice == "1":
    temp = input("Please Enter the Temperature in Fahrenheit")
    try:
        num_temp = int(temp)
        conv_temp = (num_temp - 32)/1.8
    except Error:
        print("Invalid Input, Please Enter a Valid Number")
    print(f"{temp}° in Celsius is {conv_temp}")
elif choice == "Option 2" or choice == "2":
    temp = input("Please Enter the Temperature in Celsius")
    try:
        num_temp = int(temp)
        conv_temp = (num_temp * 1.8) + 32
    except Error:
        print("Invalid Input, Please Enter a Valid Number")
    print(f"{temp}° in Fahrenheit is {conv_temp}")