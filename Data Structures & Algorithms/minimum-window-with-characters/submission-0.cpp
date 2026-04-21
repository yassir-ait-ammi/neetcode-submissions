class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> table;
        int need = t.size();
        for (int i = 0; i < need; i++) table[t[i]]++;
        int s_size = s.size();
        int left = 0, start = 0;
        int min_len = INT_MAX;
        for (int right = 0; right < s_size; right++)
        {
            if (table[s[right]] > 0)
                need--;
            table[s[right]]--;
            while (need == 0)
            {
                if (right - left + 1 < min_len)
                {
                    min_len = right - left + 1;
                    start = left;
                }
                table[s[left]]++;
                if (table[s[left]] > 0)
                    need++;
                left++;
            }
        }
        return min_len == INT_MAX ? "" : s.substr(start, min_len);
    }
};
