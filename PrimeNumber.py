for number in range(2,100):
    prime = True
    for i in range(2,number):
        if (number%i==0):
            prime = False
    if prime:
       print (number, "is a prime number.")