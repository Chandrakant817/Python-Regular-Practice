"""input: string = "123001050"
output= "00012315
"""


string = "123001050"

a = ""
b = ""

for i in string:
    if i == "0":
        a += i
    else:
        b += i

print(a + b)
