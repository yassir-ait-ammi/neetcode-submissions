class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> table;
        int required = s1.size();
        for (int i = 0; i < required; i++)
            table[s1[i]]++;
        int left = 0;
        int size_s2 = s2.size();
        for (int right = 0; right < size_s2; right++)
        {
            if (table.find(s2[right]) != table.end())
            {
                table[s2[right]]--;
                if (table[s2[right]] >= 0)
                    required--;
            }
            if (right - left + 1 > s1.size())
            {
                if (table.find(s2[left]) != table.end())
                {
                    if (table[s2[left]] >= 0)
                        required++;
                    table[s2[left]]++;
                }
                left++;
            }
            if (required == 0)
                return true;
        }
        
        return false;
    }
};
