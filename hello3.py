# Author: Parul Mahajan (CWID: 20010763)
# Date: 09/08/2023
# Description: This is a very simple example of how to create a .py program in Pycharm IDE.
# Program asks your name, which optional, you can choose not to tell your name.
# It guesses you are feeling happy or excited or giving positive vibes
# HELLO3.py file


# Output texts to the screen :
print('Hello, World!')
print('** Welcome to Lab 01 for AAI 551-B course. This is a very simple example of how to create a .py program in Pycharm IDE **')

# Get the User Input as Name :
userName = input("Please enter your name: (optional) ")
# Check if the input name is empty
if userName == "":
    print('Since you do not wish to tell your name, lets call you: Parul')
    userName = 'Parul'

userAge = input('Please enter your age: ')

print(f'Hey, {userName}, you are {userAge} years old!')