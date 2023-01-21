# Calculate Simple Interest

"""
Formula: 

SI = (p*r*t)/100
"""

p = int(input("Principal :")) 
t = int(input("Time: ")) 
r = float(input("Rate of Interest: "))

SI = (p*r*t)/100
print(SI)