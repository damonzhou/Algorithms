#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import random
import matplotlib.pyplot as plt


def generate_data_nparray(size):
    return np.random.randint(size // 3, 2 * size, size=size)


def generate_data_list(size):
    return [random.randint(size // 3, 2 * size) for x in range(size)]


def swap(input, i, j):
    input[i], input[j] = input[j], input[i]


def less(x, y):
    return x < y


def paint_init(input_data):
    plt.ion()
    size = len(input_data)
    x = range(size)
    plt.figure(figsize=(10, 5))
    plt.title('bubble sort')
    plt.bar(x, input_data)
    plt.pause(1)
    #  plt.show()


def repaint(input_data, l, j, k):
    size = len(input_data)
    x = range(size)
    plt.clf()
    bar_list = plt.bar(x, input_data)
    bar_list[j].set_color('y')
    bar_list[j].set_alpha(0.6)
    bar_list[k].set_color('g')
    bar_list[k].set_alpha(0.6)
    for i in range(len(l)):
        bar_list[l[i]].set_edgecolor('r')
    plt.pause(0.5)
    #  plt.show()


def paint_end():
    plt.ioff()
    plt.show()
