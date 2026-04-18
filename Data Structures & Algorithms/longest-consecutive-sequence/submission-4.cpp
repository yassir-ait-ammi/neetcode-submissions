class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(), nums.end());
        int longest = 1;
        int current = 1;
        int size = nums.size();
        for (int i = 1; i < size; i++)
        {
            if (nums[i] == nums[i - 1]) continue;
            if (nums[i] == nums[i - 1] + 1)
                current++;
            else
                current = 1;
            longest = max(current, longest);
        }
        return longest;
    }
};
