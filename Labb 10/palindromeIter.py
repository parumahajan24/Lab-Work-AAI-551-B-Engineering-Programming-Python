# Author: Parul Mahajan
# Date: 12/2/2023
# Description: This program determines if a user provided word is a palindrome using loops.

def plainTest(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
        return True


def main():
    word = input("Please enter a word to test if it is a palindrome: ")
    if plainTest(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome!")


if __name__ == "__main__":
    main()
