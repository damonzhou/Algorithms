#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_list, swap
from utils import paint_init, repaint, paint_end
from quick_sort import quick_sort


def bucket_sort(input_data):
    min_num = min(input_data)
    max_num = max(input_data)
    input_len = len(input_data)

    bucket_range = (max_num - min_num) / input_len
    count_list = [[] for i in range(input_len + 1)]
    for i in input_data:
        count_list[int((i - min_num) // bucket_range)].append(i)
    input_data.clear()

    for i in count_list:
        if i is None or len(i) == 0:
            continue
        for j in quick_sort(i, 0, len(i) - 1):
            input_data.append(j)

    return input_data


def main():
    input_data = generate_data_list(20)
    print(input_data)
    output_data = bucket_sort(input_data)
    print(output_data)


if __name__ == "__main__":
    main()
