#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_list, swap
from utils import paint_init, repaint, paint_end


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result


def merge_sort(input_data):
    """
    Put the greater item to left during each comparision,
    it cost O(1) memory and O(N^2) time.
    """
    size = len(input_data)
    if size < 2:
        return input_data

    mid = size // 2
    left, right = input_data[0:mid], input_data[mid:]

    return merge(merge_sort(left), merge_sort(right))


def main():
    input_data = generate_data_list(20)
    print(input_data)
    #  paint_init(input_data)
    output_data = merge_sort(input_data)
    #  paint_end()
    print(output_data)


if __name__ == "__main__":
    main()
