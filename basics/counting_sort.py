#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_nparray, swap
from utils import paint_init, repaint, paint_end


def counting_sort(input_data, max_val):
    bucket_len = max_val + 1
    bucket = [0] * bucket_len
    input_len = len(input_data)
    sorted_index = 0
    for i in range(input_len):
        bucket[input_data[i]] += 1

    for j in range(bucket_len):
        while bucket[j] > 0:
            input_data[sorted_index] = j
            sorted_index += 1
            bucket[j] -= 1

    return input_data


def main():
    input_data = generate_data_nparray(20)
    print(input_data)
    output_data = counting_sort(input_data, 2 * len(input_data))
    print(output_data)


if __name__ == "__main__":
    main()
