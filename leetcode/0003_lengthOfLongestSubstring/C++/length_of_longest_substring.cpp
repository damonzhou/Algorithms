#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>


class Solution {
public:
    /*int lengthOfLongestSubstring(std::string s) {
        int len = s.length();
        size_t max_len = 0;
        std::string longest_substr;

        std::cout << s << ", " << len << std::endl;
        int i, j;

        if (len == 1)
            return len;

        std::string tmp;
        for (i = 0; i < len; i++) {
            for (j = i+1; j <= len; j++) {
                tmp = s.substr(i, j - i);
                std::cout << "tmp_str: " << tmp << ", " << i << ", " << j << std::endl;
                if (tmp.find(s[j]) == std::string::npos) {
                    std::cout << s[j] << " is not found in " << longest_substr << std::endl;
                    tmp = s.substr(i, j - i);
                    std::cout << "tmp_str: " << tmp << std::endl;
                    if (max_len < tmp.length()) {
                        max_len = tmp.length();
                        longest_substr = tmp;
                        std::cout << "max_len: " << max_len << std::endl;
                    }
                } else {
                    std::cout << tmp << " contains " << s[j] << ", " << i << ", " << j<< std::endl;
                    if (max_len < tmp.length()) {
                        max_len = tmp.length();
                        longest_substr = tmp;
                        std::cout << "max_len: " << max_len << std::endl;
                    }
                    break;
                }
            }
        }

        std::cout << "max_len: " << max_len << std::endl;
        return max_len;
    }*/
    int lengthOfLongestSubstring(std::string s)
    {
        //s[start,end) 前面包含 后面不包含
        int start(0), end(0), length(0), result(0);
        int sSize = int(s.size());
        while (end < sSize)
        {
            char tmpChar = s[end];
            for (int index = start; index < end; index++)
            {
                if (tmpChar == s[index])
                {
                    start = index + 1;
                    length = end - start;
                    break;
                }
            }

            end++;
            length++;
            result = std::max(result, length);
        }
        return result;
    }
    /*int lengthOfLongestSubstring(std::string s) {
        int max_len(0), start(0), end(0), tmp_max_len(0);
        int len = s.length();
        int a[128] = {0};

        while (end < len) {
            if (a[s[end]] != 0) {
                if (a[s[end]] > start) {
                    start = a[s[end]];
                }
            }
            tmp_max_len = end - start + 1;
            max_len = std::max(max_len, tmp_max_len);

            a[s[end]] = end + 1;
            end++;

        }

        return max_len;
    }*/

};

int main()
{
    std::string str = "abcbb";
    // std::string str = "aadbceafbdghijklmmmn";
    Solution *s = new Solution();
    int len = s->lengthOfLongestSubstring(str);

    std::cout << "length of longest substring: " << len << std::endl;

    if (s) delete s;

    return len;
}
