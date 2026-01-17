#slicing a string
s4="SaranyaSelvakumar"
print("The original string is:",s4) 
print("The sliced string (0-6) is:",s4[0:7])
print("The sliced string (3-8) is:",s4[3:9])
print("The sliced string (5-end) is:",s4[5:])
print("The sliced string (start-4) is:",s4[:5])
print("The sliced string (2-5) is:",s4[2:5])
print("The type of s4 is:",type(s4))

#congratulatory message using string operations

name = "Saranya"
message = name + ", Congratulations on completing the Python course!"
print(message)
print("The type of message is:", type(message))
print("The uppercase message is:", message.upper())
print("The lowercase message is:", message.lower())
print("The length of the message is:", len(message))
print("The message with replaced name is:", message.replace("Saranya", "Student"))

    