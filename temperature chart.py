def main():
    print("celsius", "fahrenheit")
    a=0
    while a<=100:
        a = a + 5
        celsiustemp = a
        fahrenheittemp = (celsiustemp *9/5+32)
        print(celsiustemp,"        ", fahrenheittemp)

main()