while True:
    print("Hello, Please Select an Option")
    print("Option 1: Fahrenheit to Celsius")
    print("Option 2: Celsius to Fahrenheit")
    choice = input("Please select Option 1 or Option 2\n")
    if choice == "Option 1" or choice == "1":
        temp_fahr = input("Please Enter the Temperature in Fahrenheit\n")
        try:
            float_temp_fahr = float(temp_fahr)
            conv_temp_fahr = (float_temp_fahr - 32)/1.8
            fin_temp_fahr = round(conv_temp_fahr, 1)
        except:
            print("Invalid Input, Please Enter a Valid Number")
        print(f"{temp_fahr}° in Celsius is {fin_temp_fahr}")
    elif choice == "Option 2" or choice == "2":
        temp_cel = input("Please Enter the Temperature in Celsius\n")
        try:
            float_temp_cel = float(temp_cel)
            conv_temp_cel = (float_temp_cel * 1.8) + 32
            fin_temp_cel = round(fin_temp_cel, 1)
        except:
            print("Invalid Input, Please Enter a Valid Number")
        print(f"{temp_cel}° in Fahrenheit is {conv_temp_cel}")
    run_again = input("Would You Like To Convert Another Number?\n").lower()
    if run_again != "yes":
        print("Goodbye!")
        break