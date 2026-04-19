class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int , int>   table;
        int size = numbers.size();
        int complete;
        for (int i = 0; i < size; i++)
        {
            complete = target - numbers[i];
            if (table.find(complete) != table.end())
                return {table[complete], i + 1};
            table[numbers[i]] = i + 1;
        }
        return {};
    }
};
