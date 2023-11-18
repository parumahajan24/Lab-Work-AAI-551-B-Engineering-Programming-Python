
# Author: Parul Mahajan
# Date: 10/7/2023
# Description: this module calls the functions defined in painterFuns.py file
def painterFunc():
    """
    General function description
    :param p1: Name: painterFunc() : contains all of your other functions
    : and Create docstrings for each of your functions
    """

def intro():
    """
    General function description
    :param p1: Name: intro : akes in no parameters and returns an integer representing the user’s choice of art and a string representing the user’s desired border
    """
    print("Welcome to the painting printer!\n\t We have many options [1,4]:")
    print("\t 1. The S.S. Satisfaction")
    print("\t 2. Mina in Repose")
    print("\t 3.Spider Men Web ")
    print("\t 4.Astronaut")

    choice = int(input("Please select a painting to print: "))
    border = input("What border would you like around your painting: ")

    return choice, border

def printHeaderFooter(border, size):
    """
    General function printHeaderFooter
    :descrition: prints the border size to be privided for each functions
    """
    print( border * size)

def sleepingCat(border):
    """
      General function description
    :param p1: Name: sleepingCat : take in border calculates the max width
    :param p2: border
    :return: retunrs the photo with border and ASCII inside
    :param border:
    :return:
    """
    catArt = """
    |\\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\\ (  `'-'
    '---''(_/--'  `-'\\_)
    """
   # print(catArt)
    lines = catArt.strip().split('\n')
    maxWidth = max(len(line) for line in lines)

    # print the top border:
    printHeaderFooter(border, maxWidth + 2)

    # print each line of the ascii:
    for line in lines:
        print(f"{border}{line.strip().ljust(maxWidth)}{border}")

    # print the bottom border:
    printHeaderFooter(border, maxWidth + 2)
    print("We hope you enjoy your art!\n")

    #painterMain.main()

def sailingShip(border):
    """
    General function description
    :param p1: Name: sailingShip : take in border calculates the max width
    :param p2: border
    :return: retunrs the photo with border and ASCII inside
    :param border:
    :return:
    """
    shipImage = """|    |    |
     )_)  )_)  )_)
    )___))___))___)\\
   )____)____)_____)\\\\
 _____|____|____|____\\\\\\__
 \\    Satisfaction   /
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    # print(catArt)
    lines = shipImage.strip().split('\n')
    maxWidth = max(len(line) for line in lines)

    # print the top border:
    printHeaderFooter(border, maxWidth + 2)

    # print each line of the ascii:
    for line in lines:
        print(f"{border}{line.rstrip().ljust(maxWidth)}{border}")

    # print the bottom border:
    printHeaderFooter(border, maxWidth + 2)
    print("We hope you enjoy your art!\n")
   # painterMain.main()


def spidermanWeb(border):
    """
    General function description
    :param p1: Name: spidermanWeb : take in border calculates the max width
    :param p2: border
    :return: retunrs the photo with border and ASCII inside
    :param border:
    :return:
    """
    shipImage = """|    |    |
         )_)  )_)  )_)
        )___))___))___)\\
       )____)____)_____)\\\\
     _____|____|____|____\\\\\\__
     \\    Satisfaction 2  /
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
    # print(catArt)
    lines = shipImage.strip().split('\n')
    maxWidth = max(len(line) for line in lines)

    # print the top border:
    printHeaderFooter(border, maxWidth + 2)

    # print each line of the ascii:
    for line in lines:
        print(f"{border}{line.rstrip().ljust(maxWidth)}{border}")

    # print the bottom border:
    printHeaderFooter(border, maxWidth + 2)
    print("We hope you enjoy your art!\n")
    #painterMain.main()


def astronaught(border):
    """
    General function description
    :param p1: Name: astronaught : take in border calculates the max width
    :param p2: border
    :return: retunrs the photo with border and ASCII inside
    :param border:
    :return:
    """
    shipImage = """        _..._
      .'     '.      _
     /    .-""-\   _/ \
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .'=  *=|NASA _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
  jgs    \   `\  \
          `-._/._/
        """
    # print(catArt)
    lines = shipImage.strip().split('\n')
    maxWidth = max(len(line) for line in lines)

    # print the top border:
    printHeaderFooter(border, maxWidth + 2)

    # print each line of the ascii:
    for line in lines:
        print(f"{border}{line.rstrip().ljust(maxWidth)}{border}")

    # print the bottom border:
    printHeaderFooter(border, maxWidth + 2)
    print("We hope you enjoy your art!\n")
    #painterMain.main()


def exitFunction(border):
    exitImage = """ """
    # print(catArt)
    lines = exitImage.strip().split('\n')
    maxWidth = max(len(line) for line in lines)

    # print the top border:
    printHeaderFooter(border, maxWidth + 2)

    # print each line of the ascii:
    for line in lines:
        print(f"{border}{line.rstrip().ljust(maxWidth)}{border}")

    # print the bottom border:
    printHeaderFooter(border, maxWidth + 2)


