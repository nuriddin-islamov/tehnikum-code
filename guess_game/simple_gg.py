import random
x = int(random.randrange(1, 100))
print(f"{x} is the right answer. DO NOT COPY!")

print('Guess from 1 to 100')
usr = int(input("Guess: "))
while x != usr:
    usr = int(input('WRONG. TRY AGAIN > '))
else:
    print('YOU WIN!')