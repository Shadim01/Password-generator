import random
print("\nYou can generate a password using this!\n")
lower = "abcdefghijklmnopqrstuvwxyz"
uper = "ABCDEFGHIJKLMNOPQRSTUVSWXYZ"
number = "123456789"
symbol = "!{}[]()*/,:;'-_@'"

total = 2*(lower + uper + number + symbol)

l = int(input("Length of the password :"))

password = "".join(random.sample(total,l))
print(f"Your password : {password}")
