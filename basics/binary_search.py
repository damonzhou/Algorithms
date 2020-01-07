#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_list
from bubble_sort import bubble_sort
from quick_sort import quick_sort


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def main():
    input_data = generate_data_list(20)
    print(input_data)
    #  output_data = bubble_sort(input_data)
    output_data = quick_sort(input_data, 0, len(input_data) - 1)
    print(output_data)

    item = 5
    ret = binary_search(output_data, item)
    if ret is None:
        print('%d not found' % item)
    else:
        print('%d is found at %d' % (item, ret))


if __name__ == "__main__":
    main()
