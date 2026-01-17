#string operationson Congratulations! message to Heman
#input a word
text = str(input("Enter a string: "))   
# Concatenate " Congratulations! " to the input string
text = text + " Congratulations!"
print("The final message is:")
print(text)
print("The type of text is:", type(text))
#String Operations
s1="Hello"
s2="Heman"
s3=s1 + " " + s2
print("The concatenated string is:",s3)
print(s1+s2)
print("The length of the concatenated string is:",len(s3))
print("The uppercase string is:",s3.upper())
print("The lowercase string is:",s3.lower())
print("The string with replaced characters is:",s3.replace("Heman","Codingal"))
print("The type of s3 is:",type(s3))
#slicing a string
s4="Programming"
print("The original string is:",s4)

print("The sliced string (0-6) is:",s4[0:7])
print("The sliced string (3-8) is:",s4[3:9])    
print("The sliced string (5-end) is:",s4[5:])
print("The sliced string (start-4) is:",s4[:5])
print("The type of s4 is:",type(s4))



