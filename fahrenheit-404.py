while True:
    print("Hello, Please Select The Temperature You Want To Convert")
    print("Option 1: Fahrenheit")
    print("Option 2: Celsius")
    print("Option 3: Kelvin")
    from_temp = input("Please select Option 1, Option 2, or Option 3\n")
    print("Please, Select The Temperature You Would Like to Convert to")
    print("Option 1: Fahrenheit")
    print("Option 2: Celsius")
    print("Option 3: Kelvin")
    to_temp = input("Please select Option 1, Option 2, or Option 3\n")
    if from_temp == "1" and to_temp == "2":
        f_to_c = input("Please Enter the Temperature in Fahrenheit\n")
        try:
            float_f_to_c = float(f_to_c)
            conv_f_to_c = (float_f_to_c - 32)/1.8
            fin_f_to_c = round(conv_f_to_c, 1)
            print(f"{f_to_c}° in Celsius is {fin_f_to_c}°")
        except:
            print("Invalid Input, Please Enter a Valid Number")
    elif from_temp == "1" and to_temp == "3":
        f_to_k = input("Please Enter the Temperature in Fahrenheit\n")
        try: 
            float_f_to_k = float(f_to_k)
            conv_f_to_k = (float_f_to_k - 32)/1.8 + 273.15
            fin_f_to_k = round(conv_f_to_k, 1)
            print(f"{f_to_k}° in Kelvin is {fin_f_to_k} K")
        except:
            print("Invalid Input, Please Enter a Valid Number")
    elif from_temp == "2" and to_temp == "1":
        c_to_f = input("Please Enter the Temperature in Celsius\n")
        try:
            float_c_to_f = float(c_to_f)
            conv_c_to_f = (float_c_to_f * 1.8) + 32
            fin_c_to_f = round(conv_c_to_f, 1)
        except:
            print("Invalid Input, Please Enter a Valid Number")
        print(f"{c_to_f}° in Fahrenheit is {fin_c_to_f}")
    elif from_temp == "2" and to_temp == "3":
        c_to_k = input("Please Enter the Temperature in Celsius\n")
        try:
            float_c_to_k = float(c_to_k)
            conv_c_to_k = (float_c_to_k + 273.15)
            fin_c_to_k = round(conv_c_to_k, 1)
            print(f"{c_to_k}° in Kelvin is {fin_c_to_k} K")
        except:
            print("Invalid Input, Please Enter a Valid Number")
    elif from_temp == "3" and to_temp == "1":
        k_to_f = input("Please Enter the Temperature in Kelvin\n")
        try:
            float_k_to_f = float(k_to_f)
            conv_k_to_f = (float_k_to_f - 273.15) * 1.8 + 32
            fin_k_to_f = round(conv_k_to_f, 1)
            print(f"{k_to_f} K in Fahrenheit is {fin_k_to_f}°")
        except:
            print("Invalid Input, Please Enter a Valid Number")
    elif from_temp == "3" and to_temp == "2":
        k_to_c = input("Please Enter the Temperature in Kelvin\n")
        try: 
            float_k_to_c = float(k_to_c)
            conv_k_to_c = (float_k_to_c - 273.15)
            fin_k_to_c = round(conv_k_to_c, 1)
            print(f"{k_to_c} K in Celsius is {fin_k_to_c}°")
        except:
            print("Invalid Input, Please Enter a Valid Number")
    run_again = input("Would You Like To Convert Another Number?\n").lower()
    if run_again != "yes":
        print("Goodbye!")
        break