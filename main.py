import sys, os


def check_agrs(out):
    """Manage case no file provided if no file give , please crash programm voluntary
    printing a special info message for the user
    """

    if len(out) < 2:
        raise AttributeError(
            "\n\n::::::\nYou should pass the name of the file while calling the program\n::::::\n\n"
        )


def check_file(fn):
    """if the file does exist crash volntary the program ..."""

    if not os.path.isfile(fn):
        raise AttributeError("\n\n::::::\nThis file do not exists\n::::::\n\n")


def main():
    """main function of the program"""

    # gather calling parametres of the progamm call
    out = sys.argv

    # check_agrs
    check_agrs(out)

    # Extract the file
    my_file = out[1]

    # check_file
    check_file(my_file)

    print(f"{my_file} is a valid file ")

    ############################################
    # PERFORM COMPUTATION

    # ADD SOME CODE HERE
    ############################################

    ############################################
    # SAVE THE PREDICTIONS !

    # ADD SOME CODE HERE
    ############################################

    print("WE DONE BRO! ")


if __name__ == "__main__":
    # whats """if __name__ == "__main__":""" stands for :
    # if i write python3 main.py
    # Execute this code
    main()
