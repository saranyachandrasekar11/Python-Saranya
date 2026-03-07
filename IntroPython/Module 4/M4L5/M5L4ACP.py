#List Comprehension Practice
#Perform List Comprehension to get mentioned results.
#1. Get the list of squares of numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print(squares)
#2. Get the list of even numbers from 1 to 20.
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)
#3. Get the list of uppercase letters from a given string.
input_string = "Hello World"
uppercase_letters = [char for char in input_string if char.isupper()]
print(uppercase_letters)
#4. Get the list of words in a sentence that start with a specific letter (e.g., 'a').
sentence = "A quick brown fox jumps over a lazy dog"


specific_letter = 'a'
words_starting_with_letter = [word for word in sentence.split() if word.lower().startswith(specific_letter)]
print(words_starting_with_letter)
#5. Get the list of tuples containing numbers and their squares for numbers from 1 to 5.
number_square_tuples = [(x, x**2) for x in range(1, 6)]
print(number_square_tuples)


#Take a number from the user, create a list with all the odd numbers under the input value and another list of odd numbers.
user_number = int(input("Enter a number: "))
odd_numbers_under_input = [x for x in range(1, user_number) if x % 2 != 0]
odd_numbers = [x for x in range(1, user_number + 1) if x % 2 != 0]

#2. Create a list of fruits. Then, convert the first letter of every element to capital and create a new list of updated values.
fruits = ["apple", "banana", "cherry", "date"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)
