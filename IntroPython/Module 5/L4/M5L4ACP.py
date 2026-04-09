class StringReverser:
    def reverse_words(self, text: str) -> str:
        # split() handles multiple spaces and removes leading/trailing whitespace
        words = text.split()
        # reverse the list of words and join them with a single space
        return " ".join(reversed(words))

# Example usage:
reverser = StringReverser()
input_string = "hello world from python"
print(f"Original: {input_string}")
print(f"Reversed: {reverser.reverse_words(input_string)}")
