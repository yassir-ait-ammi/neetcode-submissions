class Solution {
public:

    string encode(vector<string>& strs) {
        int size = strs.size();
        string tmp, result;
        for (int i = 0; i < size; i++)
        {
            tmp = "";
            for (int j = 0; j < strs[i].size(); j++)
                tmp.push_back(strs[i][j] - 10);
            result += tmp;
            result += ('\n' - 10);
        }
        return result;
    }

    vector<string> decode(string s) {
        int size = s.size();
        string tmp = "";
        vector<string> result;
        char c;
        for (int i = 0; i < size; i++)
        {
            c = s[i] + 10;
            if (c != '\n')
                tmp.push_back(c);
            else
            {
                result.push_back(tmp);
                tmp = "";
            }
        }
        return result;
    }
};
