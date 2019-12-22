import sys
from math import pi


print("Hello World!")

song = ("\nTwinkle, twinkle, little star,\nHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond int he sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what yopu are!")

print(song)

# print("\nPython Version")
# print(sys.version)
# print("Version Info")
# print(sys.version_info)

r = float(input("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
