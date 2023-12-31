student = {
    "Ajau":100,
    "Raj":50,
    "vijay":70}

# Taking only Keys and then -> Convert to list
l1 = list(student.keys())

# Then use slice [-1] for last element

print(l1[-1],"-->",student[l1[-1]])