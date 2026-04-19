class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int size = s.size();
        int left = 0;
        int right = 0;
        int max_word = 0;
        string tmp;
        while (right < size)
        {
            if (tmp.find(s[right]) != string::npos)
            {
                tmp.erase(0, 1);
                left++;
            }
            else
            {
                tmp += s[right];
                max_word = max(max_word, right - left + 1);
                right++;
            }
        }
        return max_word;
    }
};
