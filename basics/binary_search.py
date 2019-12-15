#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data
from bubble_sort import bubble_sort


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
    input_data = generate_data(20)
    print(input_data)
    output_data = bubble_sort(input_data)
    print(output_data)

    item = 5
    ret = binary_search(output_data, item)
    if ret is None:
        print('%d not found' % item)
    else:
        print('%d is found at %d' % (item, ret))


if __name__ == "__main__":
    main()
