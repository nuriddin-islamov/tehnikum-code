from datetime import time

hello = input("""Hey, I am MAHMOOOOD. What is your name?
> """)
print(f"Hello, {hello}")

# m_or_f = input.upper()("""What is your gender? (type in egnlish!)
# >>""")

demographics_info = int(input("""Now tell me your birth year and I will calculate your age...
>"""))

print("So you are " + str(2020 - demographics_info) + " years old.")

if int(2020 - demographics_info) >= 18:
    print("Good. Ask me a math question - just type two numbers.")
else:
    print("You have to be at least 18 years old. GOODBYE!)")
    raise SystemExit

math_input1 = int(input("""
> Your first number - 
"""))
math_input2 = int(input("""
> Your second number - 
"""))

print("Now see the results below.")
print(f"""
SUM of your numbers is {math_input1 + math_input2}
SUBTRACTION of your numbers is {abs(math_input1 - math_input2)}
MULTIPLICATION of your numbers is {math_input2 * math_input1}
""")
import time

time.sleep(5)

gender = input("""Hey stop, now tell me your gender
> """)
while True:
    gender = input("""Hey stop, now tell me your gender
    > """)
    if gender.lower() == "female" or gender.lower() == "f" or gender.lower() == "girl":
        print("Nice, confirm your age")
    elif gender.lower() == "male" or gender.lower() == "m" or gender.lower() == "boy":
        print("You are not the girl I was looking for!")
        raise SystemExit
    else:
        print("type a correct form of gender. example: 'M' for male; 'F' for female")
        input()


age_confirm = input("> ")
if int(age_confirm) >= 18:
    print("Sexy, I love you!")
else:
    print("BYE, you are toooooo young!")
    raise SystemExit
