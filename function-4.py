def str_rev(s):
    str1 = ""
    index = len(s)

    while index > 0:
        str1 += s[index - 1]
        index = index - 1

    return str1

str1 = input("Enter a string: ")
print("The reverse string is:", str_rev(str1))


def Triangle():
    # Add the implementation of the Triangle function here
    pass  # Placeholder, add your code for the Triangle function

# Call the Triangle function here
Triangle()
