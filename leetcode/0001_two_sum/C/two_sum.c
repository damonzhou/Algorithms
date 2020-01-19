#include <stdio.h>
#include <stdlib.h>

#include "hash_table.h"

/**
 *  * Note: The returned array must be malloced, assume caller calls free().
 *   */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* ret = (int *)malloc(sizeof(int) * 2);

    for (int i = 0; i < numsSize; i++) {
        int a = nums[i];
        int b = target - a;
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[j] == b) {
                ret[0] = i;
                ret[1] = j;
                *returnSize = 2;
                return ret;
            }
        }
    }

    *returnSize = 0;
    return ret;
}


int main() {
    int input_array[] = {2, 7, 11, 15};
    int target = 18;

    int ret_size = 0;
    int num_size = sizeof(input_array) / sizeof(int);

    int* ret_indexs = twoSum(input_array, num_size, target, &ret_size);

    if (ret_size > 0) {
        printf("%d + %d = %d\n", input_array[ret_indexs[0]], input_array[ret_indexs[1]], target);
    } else {
        printf("Failed to find two numbers that compose target: %d!\n", target);
    }

    if (ret_indexs)
        free(ret_indexs);

    return 0;
}
