# Author: Parul Mahajan
# Date: 12/2/2023
# Description: This program determines if a user provided word is a palindrome using recursive function

def plainTest(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        # print(f"Word: {word[0]}")
        return False
    else:
        return plainTest(word[1:-1])


def main():
    word = input("Please enter a word to test if it is a palindrome: ")
    if plainTest(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome!")


if __name__ == "__main__":
    main()
