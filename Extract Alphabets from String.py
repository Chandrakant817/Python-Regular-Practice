# Extract Alphabets from the String

x = input("Enter the String: ")

empty =" "

for i in x:
  if i.isalpha():
    empty+=i
  else:
    continue
print(empty)