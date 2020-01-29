#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>


class Solution {
public:
    double findMedian(std::vector<int>& nums) {
        int len = nums.size();

        if (len % 2 == 0) {
            std::cout << nums[len / 2] << ", " << nums[len / 2 - 1] <<std::endl;
            return (nums[len / 2] + nums[len / 2 - 1]) / 2.0;
        } else {
            return (nums[len / 2]);
        }
    }
    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::vector<int> nums3;
        if (nums1.size() == 0 && nums2.size() == 0) return 0xffffffff;
        if (nums1.size() == 0) {
            return findMedian(nums2);
        }
        if (nums2.size() == 0) {
            return findMedian(nums1);
        }
        int index1 = 0;
        int index2 = 0;
        while (index1 < nums1.size() || index2 < nums2.size()) {
            if (index1 >= nums1.size()) {
                nums3.push_back(nums2[index2++]);
            } else if (index2 >= nums2.size()) {
                nums3.push_back(nums1[index1++]);
            } else
            if (nums1[index1] < nums2[index2]) {
                nums3.push_back(nums1[index1++]);
            } else {
                nums3.push_back(nums2[index2++]);
            }
        }

        std::cout << nums3[0] << ", " << nums3[1] << ", " << nums3[2] << ", " << nums3[3] << std::endl;
        return findMedian(nums3);
    }
};

class Solution_1 {
public:
    int findKthElm(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        int l = std::max(0, int(k - nums2.size())), r = std::min(k, int(nums1.size()));
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums2[k - m - 1] > nums1[m]) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        int nums1LeftMax = l == 0? INT_MIN : nums1[l - 1];
        int nums2LeftMax = l == k? INT_MIN : nums2[k - l - 1];
        int ret = std::max(nums1LeftMax, nums2LeftMax);
        std::cout << ret << std::endl;
        return ret;
    }

    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        int total = nums1.size() + nums2.size();

        if (total & 1) {
            return findKthElm(nums1, nums2, (total >> 1) + 1);
        } else {
            return (findKthElm(nums1, nums2, total >> 1) + findKthElm(nums1, nums2, (total >> 1) + 1)) / 2.0;
        }
    }

};

int main()
{
    const int num1[] = {3, 4, 5, 8};
    const int num2[] = {1, 2, 7};
    std::vector<int> num1_vec(num1, num1 + sizeof(num1) / sizeof(int));
    std::vector<int> num2_vec(num2, num2 + sizeof(num2) / sizeof(int));
    Solution_1 *s = new Solution_1();
    double median = s->findMedianSortedArrays(num1_vec, num2_vec);

    std::cout << "Median of two arrays: " << median << std::endl;

    if (s) delete s;

    return 0;
}
