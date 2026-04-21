class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int left = 0;
        int size = nums.size();
        vector<int> result;
        while (left + k <= size)
        {
            auto max = max_element(nums.begin() + left, nums.begin() + left + k);
            result.push_back(*max);
            left++;
        }
        return result;
    }
};
