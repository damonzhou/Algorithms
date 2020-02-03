#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_list, swap, less
from utils import paint_init, repaint, paint_end


def partition(input_data, lo, hi):
    i = lo
    j = hi + 1
    v = input_data[lo]

    while True:
        while True:
            i += 1
            if not less(input_data[i], v):
                break
            if i == hi:
                break
        while True:
            j -= 1
            if not less(v, input_data[j]):
                break
            if j == lo:
                break
        if i >= j:
            break
        repaint(input_data, [lo, hi], i, j)
        swap(input_data, i, j)
        repaint(input_data, [lo, hi], j, i)

    repaint(input_data, [lo, hi], lo, j)
    swap(input_data, lo, j)
    repaint(input_data, [lo, hi], j, lo)

    return j


def partition_1(input_data, lo, hi):
    pivot = lo
    index = pivot + 1
    i = index
    while i <= hi:
        if input_data[i] < input_data[pivot]:
            repaint(input_data, [lo, hi], i, index)
            swap(input_data, i, index)
            repaint(input_data, [lo, hi], index, i)
            index += 1
        i += 1
    repaint(input_data, [lo, hi], pivot, index - 1)
    swap(input_data, pivot, index - 1)
    repaint(input_data, [lo, hi], index - 1, pivot)
    return index - 1


def quick_sort(input_data, lo, hi):
    if hi <= lo:
        return input_data

    j = partition_1(input_data, lo, hi)
    quick_sort(input_data, lo, j - 1)
    quick_sort(input_data, j + 1, hi)

    return input_data


def main():
    input_data = generate_data_list(20)
    print(input_data)
    paint_init(input_data)
    output_data = quick_sort(input_data, 0, len(input_data) - 1)
    paint_end()
    print(output_data)


if __name__ == "__main__":
    main()
