#Write a program to convert a decimal number into a binary number?
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # Remove the '0b' prefix
print(f"The binary representation of {decimal} is {binary}.")