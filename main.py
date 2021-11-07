import sys
import importlib

from TK_1 import input_data
from TK_2 import get_min_and_max
from TK_3 import get_new_list
from TK_4 import get_new_list_1


def main():
    n = int(input("Enter number of elements : "))
    main_list = input_data(n)
    print(get_min_and_max(main_list))
    print(get_new_list(main_list))
    print(get_new_list_1(main_list))
    print(importlib.import_module('TK-5').get_new_list_square(main_list))


if __name__ == "__main__":
    sys.exit(main())
