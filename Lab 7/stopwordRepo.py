# Author: Parul Mahajan
# Date: 11/4/2023
# Description: this will create a repo to store stopwords and ask user to choose from 4 options to add, read or display the stopwords

import pickle
import os

# global constant for pickling
PICKLE_FILE_NAME = 'stopwordset.data'

def readStopWordsFile(wordSet):
    """
    This function takes a set, If the word is already in the Set, report it to the user
    Otherwise add the word to the Set
    :param wordSet: an empty set to have words from the file stopwords
    """
    while True:
        filename = input("Please enter the name of the new stopwords file:")
        # please change the filepath accordingly
        filepath = "C:\\Users\\pmahaja4\\Desktop\\Python AAI 551\\LabAssignment7\\"
        filepath += filename
        # print(filepath)
        if not os.path.exists(filepath):
            print(f"{filename} does not exist!")
        else:
            # break and proceed to read the file
            break

    with open(filepath, 'r') as myFile:
        for line in myFile:
            cleanWord = line.strip()
            if cleanWord in wordSet:
                print(f"We already have the word: {cleanWord}")
            else:
                wordSet.add(cleanWord)

def writeStopWordsFile(wordSet):
    """
    This function takes in a set, Prompt the user for the name of the file to be written to
    Writes each word in the Set to the file on a separate line
    :param wordSet: a set of stopwords
    """
    filename=input("Please enter the name of the stopwords file to write to:")
    with open(filename, 'w') as myFile:
        for word in sorted(wordSet):
            myFile.write(word + '\n')

def displayStopWords(wordSet):
    """
    This function State the number of stopwords currently in the Set
    Output each word to the screen on a separate line
    :param wordSet:a set of stopwords
    """
    print(f"Currently we have {len(wordSet)} stopwords:")
    # display the stopwords
    for word in wordSet:
        print(word)

def storeStopWords(wordSet):
    """
    This function Using the global constant, open a file for binary writing
    Dump the Set to the file
    :param wordSet:a set of stopwords
    """
    with open(PICKLE_FILE_NAME, 'wb') as file:
        pickle.dump(wordSet,file)

def restoreStopWords():
    """
    This function Using the global constant, open a file for binary reading
    Load the Set in the file to a variable
    :return: the variable containing the Set of stopwords
    """
    if os.path.isfile(PICKLE_FILE_NAME):
        with open(PICKLE_FILE_NAME, 'rb') as file:
            return pickle.load(file)
    else:
        return set()

def main():
    # check if the stopwords data file exists using global constant
    if os.path.exists(PICKLE_FILE_NAME):
        # if exists. restore the stopwords set from it
        wordSet = restoreStopWords()
    else:
        # If does not exist, create an empty set
        wordSet = set()

    print("Welcome to the stopword repository!")

    while True:
        # give users options to choose from
        print("\nPlease choose from the following options:")
        print("1. Add a new list of stopwords")
        print("2. Write current set of stopwords to a file")
        print("3. Display current set of stopwords")
        print("4. Quit")

        choice = input("Please enter your choice:")

        if choice == '1':
            readStopWordsFile(wordSet)
        elif choice == '2':
            writeStopWordsFile(wordSet)
        elif choice == '3':
            displayStopWords(wordSet)
        elif choice == '4':
            # chooses to quit, store the stopwords and exit while loop
            storeStopWords(wordSet)
            print("Thank you for using the stopword repository!")
            break
        else:
            print("invalid option - please try again.")
if __name__ == "__main__":
    main()