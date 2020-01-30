#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>


class Solution {
public:
    int expandPalindrome(std::string s, int left, int right) {
        int l = left, r = right;

        while (l >= 0 && r < s.length() && s[r] == s[l]) {
            l--;
            r++;
        }

        return r - l - 1;
    }

    std::string longestPalindrome(std::string s) {
        int len = s.length();
        if (len == 0 || len == 1) return s;

        int start = 0, end = 0;
        int max_len = 0;
        for (int i = 0; i < len; i++) {
            int len1 = expandPalindrome(s, i, i);
            int len2 = expandPalindrome(s, i, i + 1);
            max_len = std::max(std::max(len1, len2), max_len);
            if (max_len > end - start + 1) {
                start = i - (max_len - 1) / 2;
                end = i + max_len / 2;
            }
        }

        return s.substr(start, max_len);
    }

};

int main()
{
    std::string str = "abcbb";
    // std::string str = "aadbceafbdghijklmmmn";
    Solution *s = new Solution();
    std::string p = s->longestPalindrome(str);

    std::cout << "longest palindrome: " << p << std::endl;

    if (s) delete s;

    return 0;
}
