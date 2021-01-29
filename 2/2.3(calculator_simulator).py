"""
Calculator Simulator™
This is an official computer program created by Nuriddin Islamov© on 29th of January 2021. You do not need
any licence for using it. Feel free to share with your friends or just hanging out and playing with it.
Enjoy!
"""

import time

time.sleep(0.4)
user_name = input('''Hello there! Are you looking to calculate some stuff?
\nOkay, then type your name here: ''')

print(f"\nThat's what I want, {user_name.capitalize()}!")

time.sleep(0.6)

print("Let's continue...")
time.sleep(0.3)
print("Downloading some data...")
time.sleep(0.9)
print('Done!')


print("\nI am a calculator and I can calculate anything you want!")
while True:
    try:
        first_number = int(input("\nJust try me out. Type your first number > "))
        second_number = int(input('Now the second > '))
        operator_input = input("""Now tell me what do you wanna do with these numbers?
[+] - add
[-] - subtract
[*] - multiply
[/] - divide 
..>> """)
        while True:
            if operator_input != '+' and operator_input != '-' and operator_input != '*' and operator_input != '/':
                operator_input = input('Please write one of the correct operators: ')
                continue
            else:
                break

        if operator_input == '+':
            result = first_number + second_number
            print(f'\nResult: {first_number} added to {second_number} is {result}')
            print('Thank you for trying me out!')
            break
        elif operator_input == '-':
            result = first_number - second_number
            print(f'\nResult: {first_number} minus {second_number} is {result}')
            print('Thank you for trying me out!')
            break
        elif operator_input == '*':
            result = first_number * second_number
            print(f'\nResult: {first_number} multiplied by {second_number} is {result}')
            print('Thank you for trying me out!')
            break
        elif operator_input == '/':
            result = first_number / second_number
            print(f'\nResult: {first_number} divided by {second_number} is {result}')
            print('Thank you for trying me out!')
            break
    except ZeroDivisionError:
        print('YOU CANNOT DIVIDE A NUMBER BY ZERO')
        print('Try again with new numbers! ')
        continue
    except ValueError:
        print("Type a number when the program asks for a number! DO NOT BE SILLY!")
        continue
