# Author: Parul Mahajan
# Date: 11/3/2023
# Description: This file contains 3 fucntions, readTextFile(), outputFreq() and main(). It reads
# the file in readTextFile() and counts the frequency and outputs the same in outputFreq()
#  in main() rest of the functions are called with appropriate parameter
import os
def readTextFile(wordDict):
    """
    This function takes in a Dictionary as a parameter and returns nothing but reads in the file and calculate
    the frequency of each word in it.
    :param wordDict: an empty dictionary that will be filled with word and its count later on
    """
    while True:
        filename = input("Please enter the name of the file to analyze:")
        # please change the filepath accordingly
        filepath = "C:\\Users\\pmahaja4\\Desktop\\Python AAI 551\\LabAssignment7\\"
        filepath += filename
        # print(filepath)
        if not os.path.exists(filepath):
            print(f"{filename} does not exist!")
        else:
            # break and proceed to read the file
            break
    with open(filename, 'r') as myFile:
        for line in myFile:
            cleanFile = line.strip().lower()
            # split the lines into words
            words = cleanFile.split()
            # print(words)
            for x in words:
                wordDict[x] = wordDict.get(x, 0) + 1
    # for word in wordDict.items():
    #     print(word)

def outputFreq(wordDict):
    """
    This function takes in a dictionary and prints the unique words and count of each word in it
    :param wordDict: a dictionary having words that were in the file read in readTextFile()
    """
    print(f"The file contained {len(wordDict)} unique words.")
    for word, count in wordDict.items():
        print(f"{word}:{count}")

def main():
    """
    This is the main function which creates an empty dictionary, and calls readTextFile() and outputFreq()
    passing the empty dictionary
    """
    # create empty dictionary
    wordDict = {}
    readTextFile(wordDict)
    outputFreq(wordDict)

if __name__ == "__main__":
    main()