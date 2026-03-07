#Check the frequency
#Check the frequency of a value in the given test dictionary.
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
K = 2
frequency = sum(1 for value in test_dict.values() if value == K)
print(f"Frequency of {K} is: {frequency}")


# Alternative method using list comprehension
test_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
target_value = 10
count = 0
for value in test_dict.values():
    if value == target_value:
        count += 1
print(f"The value {target_value} appears {count} times.")
