class RomanConverter:
    def __init__(self):
        # List of tuples containing the integer value and its Roman symbol
        # Ordered from largest to smallest for the greedy algorithm
        self.val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

    def int_to_roman(self, num: int) -> str:
        roman_num = ""
        for value, symbol in self.val_map:
            # While the number is greater than or equal to the current value, 
            # append the symbol and subtract the value
            while num >= value:
                roman_num += symbol
                num -= value
        return roman_num

# Example usage:
converter = RomanConverter()
number = 1994
print(f"Integer: {number}")
print(f"Roman Numeral: {converter.int_to_roman(number)}")
