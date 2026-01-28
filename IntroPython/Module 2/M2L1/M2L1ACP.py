#Write a program to check the age entered by the user is between 10 to 20 years or not? using nested loops
age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("Age is between 10 and 20.")
    else:
        print("Age is greater than 20.")
else:
    print("Age is less than 10.")