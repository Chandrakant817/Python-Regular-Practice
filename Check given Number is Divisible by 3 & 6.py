# Check given Number is Divisible by 3 & 6

num = int(input("Enter the Number: "))

if num%3 == 0 and num%6 == 0:
  print(num, "Number is Divisible by 3 and 6")
else:
  print(num, "Number is Not Divisible by 3 and 6")