#Write a program to calculate how many total digits are in a number entered by the user?
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Total digits in the number:", count)