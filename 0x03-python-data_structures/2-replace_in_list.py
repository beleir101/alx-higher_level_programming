#!/usr/bin/python3
""" Replaces the element at index idx"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list


if __name__ == "__main__":
    pass
