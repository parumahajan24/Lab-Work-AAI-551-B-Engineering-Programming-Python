# Author: Parul Mahajan
# Date: 12/2/2023
# Description: This program determines if a series of ( and ) are balanced.

# global variable 'count'
COUNT = 0


def parenTest(line, position):
    global COUNT
    if position == len(line):
        return COUNT == 0
    if line[position] == '(':
        COUNT += 1
    elif line[position] == ')':
        if COUNT > 0:
            COUNT -= 1
        else:
            return False
    return parenTest(line, position + 1)


def main():
    user_input = input("Please enter a series of parenthesis to see if they are balanced:")
    if parenTest(user_input, 0):
        print(f"{user_input} is balanced.")
    else:
        print(f"{user_input} is not balanced.")


if __name__ == "__main__":
    main()
