import re, random
import colorama
from colorama import Fore, init


init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Hawaii"],
    "mountains": ["Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel more? Sense of all their hot spots!"
]

def normalize_input(text):
    return re.sub(r'\s+', ' ', text).strip().lower()


def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ").strip()
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (y/n)")
        answer = input(Fore.YELLOW + "You: ").lower().strip()

        if answer == 'y':
            print(Fore.GREEN + f"TravelBot: Enjoy {suggestion}!")
        else:
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        show_help()


def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: ").strip())
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ").strip()

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "* Pack versatile clothes")
    print(Fore.GREEN + "* Bring chargers/adapters")
    print(Fore.GREEN + "* Check the weather forecast.")


def tell_joke():
    print(Fore.YELLOW + "TravelBot: " + random.choice(jokes))


def show_help():
    print(Fore.MAGENTA + "\n--- Help ---")
    print(Fore.GREEN + "* Suggest travel ideas (say \"recommendation\")")
    print(Fore.GREEN + "* Offer packing tips (say \"packing\")")
    print(Fore.GREEN + "* Tell a joke (say \"joke\")")
    print(Fore.CYAN + "* Type \"exit\" or \"bye\" to end chat.\n")


def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Welcome, {name}!")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"[{name}] > ").strip()
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")
            show_help()

chat()
