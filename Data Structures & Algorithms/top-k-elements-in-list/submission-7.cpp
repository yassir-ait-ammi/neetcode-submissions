class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> table;
        int size = nums.size();
        for (int i = 0; i < size; i++)
            table[nums[i]]++;
        auto it = table.begin();
        vector<int> tmp;
        while (it != table.end())
        {
            if (find(tmp.begin(), tmp.end(), it->second) == tmp.end())
                tmp.push_back(it->second);
            it++;
        }
        sort(tmp.begin(), tmp.end(), greater<int>());
        vector<int> result;
        for (int i = 0; i < tmp.size() && result.size() < k; i++)
        {
            it = table.begin();
            while (it != table.end() && result.size() < k)
            {
                if (it->second == tmp[i])
                {                    
                    result.push_back(it->first);
                }
                it++;
            }
        }
        return result;
    }
};