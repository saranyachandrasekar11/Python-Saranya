#create an ASCII Value Checker that reveals the secret numeric code behind every character. Every letter, digit, and symbol on your keyboard has a unique number assigned to it in the ASCII system.

def ascii_value_checker():
    print("Welcome to the ASCII Value Checker!")
    user_input = input("Please enter a character: ")
    
    if len(user_input) != 1:
        print("Error: Please enter exactly one character.")
        return
    
    ascii_value = ord(user_input)
    print(f"The ASCII value of '{user_input}' is: {ascii_value}")   


ascii_value_checker()





                                