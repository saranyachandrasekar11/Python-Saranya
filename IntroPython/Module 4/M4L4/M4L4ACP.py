#Set Symmetric Difference
#Write a Python program to find the symmetric difference between two sets.
setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nSymmetric difference of two said sets:")
setz = setx.symmetric_difference(sety)
print(setz)