# Check 3 angles can form a Triangle or Not

a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))

if a+b+c == 180 and a!=0 and b!=0 and c!=0:
  print("Possible")
else:
  print("Not Possible")