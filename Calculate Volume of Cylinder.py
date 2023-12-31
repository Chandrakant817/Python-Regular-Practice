# Calculate Volume of Cylinder

"""
Formula:

Volume = 3.14 * (r**2) * h
"""

h = float(input("Enter the Height: "))
r = float(input("Enter the Radius: "))

Volume = 3.14 * (r**2) * h
print("Volume of Cylinder :",Volume)

# Cost of 1 liter milk is rs 40.
Cost = Volume/1000 * 40
print("Cost of Milk is :",Cost)