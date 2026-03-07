# Check if tuple is a palindrome
tuple1 = (1, 2, 3, 3, 2, 1)

if tuple1 == tuple1[::-1]:
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")