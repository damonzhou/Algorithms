#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in nums_hash:
                return [i, nums_hash[b]]
            nums_hash[nums[i]] = i

        return [-1, -1]


def main():
    input_arrays = [2, 7, 11, 15]
    target = 9

    s = Solution()
    ret = s.twoSum(input_arrays, target)
    print(input_arrays[ret[0]], "+", input_arrays[ret[1]], "=", target)


if __name__ == "__main__":
    main()
