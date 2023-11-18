# Author: Parul Mahajan
# Date: 10/7/2023
# Description: this module shows the ASCIi value in the form of images (3D, if your imagination is good)

def intro():
    print("Welcome to the painting printer!\n\t We have many options [1,4]:")
    print("\t 1. The S.S. Satisfaction")
    print("\t 2. Mina in Repose")
    print("\t 3.Spider Men Web ")
    print("\t 4.Astronaut")

    choice = int(input("Please select a painting to print: "))
    border = input("What border would you like around your painting: ")

    return choice, border

def printHeaderFooter(border, size):
    print( border * size)

def sleepingCat(border):
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
    main()

def sailingShip(border):
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
    main()


def spidermanWeb(border):
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
    main()

def astronaught(border):
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
    main()

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

def main():
   choice, border = intro()
   if choice == 1:
       sailingShip(border)
   elif choice == 2:
       sleepingCat(border)
   elif choice == 3:
       spidermanWeb(border)
   elif choice == 4:
       astronaught(border)
   else:
       exitFunction(border)
       print("Hmmmm....we don't seem to have that painting.")
       exit(-1)
main()