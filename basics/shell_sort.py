#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import generate_data_list, swap
from utils import paint_init, repaint, paint_end


def shell_sort(input_data):
    length = len(input_data)
    paint_init(input_data)
    h = 1

    while h < length // 3:
        h = 3 * h + 1

    while h >= 1:
        print('\rh = %d' % h, end='')
        for i in range(h, length):
            for j in range(i, h - 1, -h):
                if input_data[j] >= input_data[j - h]:
                    break
                repaint(input_data, [i], j, j - h)
                swap(input_data, j, j - h)
                repaint(input_data, [i], j - h, j)

        h = h // 3
        if h == 0:
            print('\rh = %d' % h)

    paint_end()
    return input_data


def main():
    input_data = generate_data_list(21)
    print(input_data)
    output_data = shell_sort(input_data)
    print(output_data)


if __name__ == "__main__":
    main()
