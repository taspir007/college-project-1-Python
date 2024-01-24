def factorial(s):
    if s == 0:
        return 1
    else:
        return s * factorial(s - 1)

s = int(input("Enter a positive number: "))

if s < 0:
    print("You entered a negative number, please try again!")
else:
    print("The factorial of", s, "is:", factorial(s))

