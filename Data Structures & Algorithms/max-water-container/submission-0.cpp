class Solution {
public:
    int maxArea(vector<int>& heights) {
        int size = heights.size();
        int left = 0, right = size - 1, max = 0;
        int tmp;
        while (left < right)
        {
            tmp =  (heights[left] < heights[right] ? heights[left] : heights[right]) * (right - left);
            max = tmp > max ? tmp : max;
            if (heights[left] < heights[right])
                left++;
            else
                right--;
        }
        return max;
    }
};
