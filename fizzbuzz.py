"""
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
and for the multiples of five print "Buzz".For numbers which are multiples of both three and five print "FizzBuzz".
"""


a, b = map(int, input().split(","))

for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:  # Check for multiples of both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Check for mulftiples of 3
        print("Fizz")
    elif i % 5 == 0:  # Check for multiples of 5
        print("Buzz")
    else:
        print(i)  # Print the number if none of the conditions above are met
        
