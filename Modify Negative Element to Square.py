# Modify Negative Element to Square

x = [2,8,-3,0,-4]
#print(x)
#srq = []

for i in x:
  if i<0:
    pos = x.index(i)
    x[pos] = x[pos]**2
    #srq.append(x[pos])
print(x)
