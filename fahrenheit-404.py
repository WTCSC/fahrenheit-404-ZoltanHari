while True:
    print("Hello, Please Select The Temperature You Want To Convert From\nOption 1: Fahrenheit\nOption 2: Celsius\nOption 3 Kelvin")
    from_temp = input("Please select Option 1, Option 2, or Option 3\n").lower()
    print("Please, Select The Temperature You Would Like to Convert To\nOption 1: Fahrenheit\nOption 2: Celsius\nOption 3 Kelvin")
    to_temp = input("Please select Option 1, Option 2, or Option 3\n").lower()
    if from_temp == to_temp:
        print("Same Unit Selected. Please Try Again")
        continue
    try:
        temp = input("Enter the Temperature You Would Like to Convert\n")
        temp_float = float(temp)
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number")
        continue
    match (from_temp, to_temp):
        case ("1", "2"):
            conv_temp = (temp_float - 32)/ 1.8
            fin_temp = round(conv_temp, 1)
            print(f"{temp}° Fahrenheit in Celsius is {fin_temp}°")
        case ("1", "3"):
            conv_temp = (temp_float - 32)/ 1.8 + 273.15
            fin_temp = round(conv_temp, 1)
            print(f"{temp}° Fahrenheit in Kelvin is {fin_temp} K")
        case ("2", "1"):
            conv_temp = (temp_float + 32)* 1.8
            fin_temp = round(conv_temp, 1)
            print(f"{temp}° Celsius in Fahrenheit is {fin_temp}°")
        case ("2", "3"):
            conv_temp = (temp_float + 273.15)
            fin_temp = round(conv_temp, 1)
            print(f"{temp}° Celsius in Kelvin is {fin_temp} K")
        case ("3", "1"):
            conv_temp = (temp_float - 273.15)* 1.8 + 32
            fin_temp = round(conv_temp, 1)
            print(f"{temp} K in Fahrenheit is {fin_temp}°")
        case ("3", "2"):
            conv_temp = (temp_float - 273.15)
            fin_temp = round(conv_temp, 1)
            print(f"{temp} K in Celsius is {fin_temp}°")
        case _: 
            print("Invalid Option")
    run_again = input("Would You Like To Convert Another Number?\n").lower()
    if run_again != "yes":
        print("Goodbye!")
        break