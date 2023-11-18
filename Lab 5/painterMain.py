# Author: Parul Mahajan
# Date: 10/7/2023
# Description: this module calls the functions defined in painterFuns.py file
import painterFuncs

def caller(choice,border):

    if choice == 1:
        painterFuncs.sailingShip(border)
        main()
    elif choice == 2:
        painterFuncs.sleepingCat(border)
        main()
    elif choice == 3:
        painterFuncs.spidermanWeb(border)
        main()
    elif choice == 4:
        painterFuncs.astronaught(border)
        main()
    else:
        painterFuncs.exitFunction(border)
        print("Hmmmm....we don't seem to have that painting.")
        exit(-1)
def main():
   choice, border = painterFuncs.intro()
   caller(choice, border)
main()