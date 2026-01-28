#Write a program to make a mirrored right-angled triangle?# Program to print a mirrored right-angled triangle
#Take input from user

rows = int(input("Enter the number of rows: ")) 
#outer loop for number of rows
for i in range(1, rows + 1):

    #inner loop for spaces
        for j in range(rows - i):
            print(" ", end="")
    #inner loop for stars
        for k in range(i):
            print("*", end="")
        print()         