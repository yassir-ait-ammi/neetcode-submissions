class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> result;
        for (int i = 0; i < size; i++)
        {
            int sum = 1;
            for (int j = 0; j < size; j++)
            {
                if (i != j)
                    sum *= nums[j];
            }
            result.push_back(sum);
        }
        return result; 
    }
};
