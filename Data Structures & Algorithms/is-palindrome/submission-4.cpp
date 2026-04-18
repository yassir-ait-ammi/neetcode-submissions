class Solution {
public:
    bool isPalindrome(string s) {
        int size = s.size();
        for (char &c : s) {
            c = tolower(static_cast<unsigned char>(c));
        }
        string against = s;
        reverse(against.begin(), against.end());
        s.erase(std::remove_if(s.begin(), s.end(), [](unsigned char c) {
             return !std::isalpha(c) && !isdigit(c);
        }), s.end());
        against.erase(std::remove_if(against.begin(), against.end(), [](unsigned char c) {
             return !std::isalpha(c);
        }), against.end());
        cout << s << " " << against;
        return s == against;
    }
};
