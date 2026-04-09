class Dog:
    # Class variable
    species = "Canis familiaris"  # All dogs belong to this species

    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {self.species}")
        print("---------------------")

# Create two instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "German Shepherd")

# Display details of the dogs
print("Details of Dog 1:")
dog1.display_details()

print("Details of Dog 2:")
dog2.display_details()