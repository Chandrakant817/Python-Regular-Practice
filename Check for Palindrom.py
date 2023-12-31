# Check for Palindrom

def is_pal(word):
  rev = word[::-1]
  if word == rev:
    return True
  else:
    return False

print(is_pal("MOM"))
#print(is_pal("Apple"))