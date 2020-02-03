#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_nparray, swap
from utils import paint_init, repaint, paint_end


def radix_sort(input_data):
    i = 0
    n = 1
    max_num = max(input_data)
    while max_num > 10 ** n:
        n += 1
    while i < n:
        bucket = {}
        for x in range(10):
            bucket.setdefault(x, [])
        for x in input_data:
            radix = int((x / (10 ** i)) % 10)
            bucket[radix].append(x)
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    input_data[j] = y
                    j += 1
        i += 1

    return input_data


def main():
    input_data = generate_data_nparray(20)
    print(input_data)
    output_data = radix_sort(input_data)
    print(output_data)


if __name__ == "__main__":
    main()
