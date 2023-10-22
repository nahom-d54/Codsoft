import string, random

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

pwlen = int(input("Inout password length: "))

pw = ''.join(random.choices(chars,k=pwlen))

print(pw)