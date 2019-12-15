#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_nparray, swap
from utils import paint_init, repaint, paint_end


def bubble_sort(input_data):
    """
    Put the greater item to left during each comparision,
    it cost O(1) memory and O(N^2) time.
    """
    size = len(input_data)
    paint_init(input_data)
    for i in range(size):
        for j in range(size - i - 1):
            repaint(input_data, [i], j, j + 1)

            if input_data[j] > input_data[j + 1]:
                #  print(input_data[j], input_data[j+1])
                swap(input_data, j, j + 1)
                #  print(input_data[j], input_data[j+1])

                repaint(input_data, [i], j + 1, j)

    paint_end()
    return input_data


def main():
    input_data = generate_data_nparray(6)
    print(input_data)
    output_data = bubble_sort(input_data)
    print(output_data)


if __name__ == "__main__":
    main()
