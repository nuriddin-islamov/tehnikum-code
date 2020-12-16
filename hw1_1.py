a = int(input("> "))
b = int(input("> "))
c = int(input("> "))

if b < a < c or b > a > c:
    print(f"{a} is the middle number")
elif a < b < c or a > b > c:
    print(f"{b} is the middle number")
else:
    print(f"{c} is the middle number")