#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_list
from utils import paint_init, repaint, paint_end


def findSmallest(input_data):
    smallest = input_data[0]
    smallest_index = 0

    for i in range(1, len(input_data)):
        if input_data[i] < smallest:
            smallest = input_data[i]
            smallest_index = i

    return smallest_index


def selection_sort(input_data):
    """
    Find the smallest item, then append it to a new array,
    it would cost O(N) memory and O(N^2) time.
    """
    output_data = []
    for i in range(len(input_data)):
        smallest_index = findSmallest(input_data)
        output_data.append(input_data.pop(smallest_index))
    return output_data


def selection_sort_inplace(input_data):
    length = len(input_data)
    paint_init(input_data)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if input_data[j] < input_data[min]:
                min = j

        repaint(input_data, [i], i, min)
        temp = input_data[i]
        input_data[i] = input_data[min]
        input_data[min] = temp
        repaint(input_data, [i], min, i)

    paint_end()

    return input_data


def main():
    input_data = generate_data_list(20)
    print(input_data)
    output_data = selection_sort_inplace(input_data)
    print(output_data)
    #  output_data = selection_sort(input_data)
    #  print(output_data)


if __name__ == "__main__":
    main()
