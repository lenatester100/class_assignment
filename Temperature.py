def main ():
    temp = int(input("Enter the temp for fahrenheit"))
    Celsius = (temp - 32) * 5.0/9.0 #assignment
    print("The temperature in fahrenheit is ")
    print("The  temperature in celsius is ")
    user = input("Would you like to continue?")
    if user == "no":
        print("another time")
    else:
        main()
main()
