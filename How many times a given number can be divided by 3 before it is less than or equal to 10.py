# How many times a given number can be divided by 3 before it is less than or equal to 10

count = 0
number = 180

while number > 10:
  number = number/3
  count+=1
print("Total iteration required: ", count)
