# Factorial of a Number

num = int(input("Enter the Number: "))
f = 1

for i in range(1,num+1):
  f = f * i
print(f)

"""
Factorial of a number using function

def fact(num):
  f = 1
  for i in range(1,num+1):
    f = f * i
  return f

fact(4)
"""