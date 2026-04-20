class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> table(26, 0);
        int size = s.size();
        int left = 0;
        int max_appears = 0, max_window = 0;
        for (int right = 0; right < size; right++)
        {
            table[s[right] - 'A']++;

            max_appears = max(max_appears, table[s[right] - 'A']);
            while ((right - left + 1) - max_appears > k)
            {
                table[s[left] - 'A']--;
                left++;
            }

            max_window = max(max_window, right - left + 1);
        }
        return max_window;
    }
};
