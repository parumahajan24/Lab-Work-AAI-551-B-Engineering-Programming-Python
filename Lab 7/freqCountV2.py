# Author: Parul Mahajan
# Date: 11/3/2023
# Description: this file contains 3 functions, readStopWordsFile(), readTextFile() and main()
# It reads in the stopwords file in readStopWordsfile() and add to a set, adn then pass it to readTextFile()
# and add the words from set to dictionary read from a file and call functions in main()

import os

def readStopWordsFile(wordSet):
    """
    This function takes an empty set, and adds word to it from stopwords file
    :param wordSet: an empty set to have words from the file stopwords
    """
    while True:
        filename = input("Please enter the name of the stopwords file:")
        # please change the filepath accordingly
        filepath = "C:\\Users\\pmahaja4\\Desktop\\Python AAI 551\\LabAssignment7\\"
        filepath += filename
        # print(filepath)
        if not os.path.exists(filepath):
            print(f"{filename} does not exist!")
        else:
            # break and proceed to read the file
            break

    with open(filepath, 'r') as stopWordFile:
        for line in stopWordFile:
            # remove extra whitespaces or newlines from the line
            cleanLine = line.strip()
            # add the line to set
            wordSet.add(cleanLine)
    # for x in wordSet:
    #     print(x)


def readTextFile(wordDict,wordSet):
    """
    This function takes in a Dictionary and a Set as parameters and returns nothing but reads in the file and calculate
    the frequency of each word in it after adding words from stopwords file(stored in wordSet parameter)
    :param wordDict: an empty dictionary that will be filled with word and its count later on
    :param wordSet: an empty set to have words from the file stopwords
    """
    while True:
        wordFilename = input("Please enter the name of the file to analyze:")
        # please change the filepath accordingly
        filepath = "C:\\Users\\pmahaja4\\Desktop\\Python AAI 551\\LabAssignment7\\"
        filepath += wordFilename
        # print(filepath)
        if not os.path.exists(filepath):
            print(f"{wordFilename} does not exist!")
        else:
            # break and proceed to read the file
            break
    with open(wordFilename, 'r') as myFile:
        for line in myFile:
            cleanFile = line.strip().lower()
            # split the lines into words
            words = cleanFile.split()
            # print(words)
            # if word not in set, add to dictionary
            for word in words:
                if word not in wordSet:
                    wordDict[word] = wordDict.get(word, 0) + 1
    # print the unique words
    print(f"The file contained {len(wordDict)} unique words.")
    # print the word and thier counts in dictionary after not adding stopwords from wordSet
    for word, count in wordDict.items():
        print(f"{word}:{count}")


def main():
    # create empty set to store stopwords
    wordSet = set()
    # create empty dictionary
    wordDict = {}
    readStopWordsFile(wordSet)
    readTextFile(wordDict,wordSet)


if __name__ == "__main__":
    main()