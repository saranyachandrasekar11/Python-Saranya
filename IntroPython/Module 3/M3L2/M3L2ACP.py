#Dhriti is facing difficulty while switching off the system. So, he designs a program that will check few conditions before shutting down a program. 

#Create a function called shutdown. Place few conditions in the function. If the input by the user is “Yes” then it will display shutting down.  And if the user enters no, then it will display abort shut down. If some other input is passed, then it is going to display “sorry.”
  
def shutdown(user_input):
  if user_input == "Yes":
    print("Shutting down...")
  elif user_input == "No":
    print("Abort shutdown.")
  else:
    print("Sorry.")
    

# Example usage:
shutdown("Yes")
shutdown("No")
shutdown("Maybe")