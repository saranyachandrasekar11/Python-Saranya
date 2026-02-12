#Write a program to calculate the customer due amount after paying a bill of a certain amount using for loop, return statement and continue statement, pass statement and break statement.
#Take user input
amount = float(input("Enter the bill amount: "))
payment = float(input("Enter the payment amount: "))
def calculate_due(amount, payment):
    if payment < amount: #condition 1
        due = amount - payment
        return due #return statement
    elif payment == amount: #condition 2
        print("No due amount. Thank you for your payment!")
        return 0 #return statement
    else: #condition 3
        change = payment - amount
        print(f"Payment exceeds the bill amount. Your change is: {change}")
        return 0 #return statement
due_amount = calculate_due(amount, payment)
if due_amount > 0: #condition 4
    print(f"You still owe: {due_amount}")
else: #condition 5
    print("Thank you for your payment!")


            