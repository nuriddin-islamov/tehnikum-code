a = int(input("> "))
b = int(input("> "))
c = int(input("> "))


if a > b >= c or a > c >= b:
    print(f"{a} is the biggest number.")
elif b > a >= c or b > c >= a:
    print(f"{b} is the biggest number.")
else:
    print(f"{c} is the biggest number.")