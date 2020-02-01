#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_nparray, swap
from utils import paint_init, repaint, paint_end


def build_max_heap(arr):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        repaint(arr, [i], i, largest)
        swap(arr, i, largest)
        repaint(arr, [i], largest, i)
        heapify(arr, largest)

def heap_sort(input_data):
    global arrLen
    arrLen = len(input_data)
    build_max_heap(input_data)
    for i in range(len(input_data) - 1, 0, -1):
        repaint(input_data, [i], 0, i)
        swap(input_data, 0, i)
        repaint(input_data, [i], i, 0)
        arrLen -= 1
        heapify(input_data, 0)

    return input_data


def main():
    input_data = generate_data_nparray(20)
    print(input_data)
    paint_init(input_data)
    output_data = heap_sort(input_data)
    paint_end()
    print(output_data)


if __name__ == "__main__":
    main()
