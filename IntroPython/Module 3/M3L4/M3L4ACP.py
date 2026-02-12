# Write a program to check the age entered by the user is correct or not.
#  If there is some error in the value of age entered. And check that the age entered by the user is even or odd.
# Use exception handling to catch the error and print the appropriate message. If there is no error in the value of age entered, then print whether the age is even or odd.

# value error

#using a try and except


def check_age():
    try:
        # Taking input from the user
        age_input = input("Please enter your age: ")
        
        # Attempting to convert the input to an integer
        age = int(age_input)

        # Logical check for negative numbers or zero
        if age <= 0:
            print("Error: Age must be a positive number greater than 0.")
        else:
            # Checking if the age is even or odd
            if age % 2 == 0:
                print(f"The age {age} is a valid Even number.")
            else:
                print(f"The age {age} is a valid Odd number.")

    except ValueError:
        # This block catches non-numeric inputs (like "twenty" or "12.5")
        print("Error: Invalid input! Please enter a whole number (e.g., 25).")

# Run the function
check_age()




