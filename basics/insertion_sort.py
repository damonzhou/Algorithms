#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_list, swap
from utils import paint_init, repaint, paint_end


def insertion_sort(input_data):
    length = len(input_data)
    paint_init(input_data)

    for i in range(length):
        for j in range(i, 0, -1):
            if input_data[j] >= input_data[j - 1]:
                break
            repaint(input_data, [i], j, j - 1)
            swap(input_data, j, j - 1)
            repaint(input_data, [i], j - 1, j)

    paint_end()
    return input_data


def main():
    input_data = generate_data_list(20)
    print(input_data)
    output_data = insertion_sort(input_data)
    print(output_data)


if __name__ == "__main__":
    main()
