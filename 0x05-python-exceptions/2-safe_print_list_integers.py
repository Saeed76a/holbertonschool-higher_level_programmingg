#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{}".format(my_list[i]), end="")
        print()
    except IndexError:
        print()
        raise
# x can be bigger than the length of my_list
    return (x)