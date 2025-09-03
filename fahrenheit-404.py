print("Hello, Please Select an Option")
print("Option 1: Fahrenheit to Celsius")
print("Option 2: Celsius to Fahrenheit")
choice = input("Please select Option 1 or Option 2")
if choice == "Option 1" or choice == "1":
    temp_fahr = input("Please Enter the Temperature in Fahrenheit")
    try:
        num_temp_fahr = int(temp_fahr)
        conv_temp_fahr = (num_temp_fahr - 32)/1.8
    except Error:
        print("Invalid Input, Please Enter a Valid Number")
    print(f"{temp_fahr}° in Celsius is {conv_temp_fahr}")
elif choice == "Option 2" or choice == "2":
    temp_cel = input("Please Enter the Temperature in Celsius")
    try:
        num_temp_cel = int(temp_cel)
        conv_temp_cel = (num_temp_cel * 1.8) + 32
    except Error:
        print("Invalid Input, Please Enter a Valid Number")
    print(f"{temp_cel}° in Fahrenheit is {conv_temp_cel}")