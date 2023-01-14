# Reverse internal Content of Each Word

Input = input("Enter the Srting: ").split()
Revser =[]

rev = Input[::-1]
#print(rev)

for word in rev:
  Revser.append(word[::-1]) 
#print(Revser)

output = " ".join(Revser)
print(output)