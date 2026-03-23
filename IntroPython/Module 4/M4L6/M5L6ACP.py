#Write a Python program to generate a random password consisting of lower case and upper case characters along with numbers. You can also use random module for shuffling the password generated.
import random
import time

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()