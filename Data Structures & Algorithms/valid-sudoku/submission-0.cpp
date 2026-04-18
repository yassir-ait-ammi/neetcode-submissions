class Solution {
public:
    bool is_valid(vector<vector<char>>& board, int row, int col, char c)
    {
        int size = board.size();
        for (int i = 0; i < size; i++)
        {
            if (i != row &&  board[i][col] == c) return false;
            if (i != col && board[row][i] == c) return false;
            int r = 3 * (row / 3) + i / 3;
            int c2 = 3 * (col / 3) + i % 3;

            if ((r != row || c2 != col) && board[r][c2] == c)
                return false;
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        int size = board.size();
        int inside_size;
        for (int i = 0; i < size; i++)
        {
            inside_size = board[i].size();
            for (int j = 0; j < inside_size; j++)
            {
                if (board[i][j] != '.' && !is_valid(board, i, j, board[i][j]))
                    return false;
            }
        }
        return true;
    }
};
