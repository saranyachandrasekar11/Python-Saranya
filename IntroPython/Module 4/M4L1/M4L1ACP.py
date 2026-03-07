
# Get range from user
start = int(input("Start: "))
end = int(input("End: "))

# Initialize empty lists
squares = []
evens = []
odds = []

# Loop through the range
for i in range(start, end + 1):
    sq = i * i
    squares.append(sq)
    
    # Check if the square is even or odd
    if sq % 2 == 0:
        evens.append(sq)
    else:
        odds.append(sq)

# Print results
print("All squares:", squares)
print("Even squares:", evens)
print("Odd squares:", odds)
