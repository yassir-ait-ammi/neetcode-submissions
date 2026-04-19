class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best_ofer = 0;
        int size = prices.size();
        for (int i = 0; i < size; i++)
        {
            auto it = std::max_element(prices.begin() + i, prices.end());
            if (*it - prices[i] > best_ofer)
                best_ofer = *it - prices[i];
        }
        return best_ofer;
    }
};
