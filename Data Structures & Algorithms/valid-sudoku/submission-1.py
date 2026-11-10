class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_squares=[set() for i in range(0,9)]
        for i in range(0,9):
            row_nums=set()
            col_nums=set()
            print('row',i)
            for j in range(0,9):
                print('column',j)
                print('row_nums',row_nums)
                if board[i][j] != '.':
                    print(f'board[{i}][{j}]',board[i][j])
                    if board[i][j] in row_nums:
                        print('changed')
                        return False
                    row_nums.add(board[i][j])
                    print('row_nums',row_nums)

                    index = (i//3)*3+(j//3)
                    if board[i][j] in sub_squares[index]:
                        print('changed')
                        return False
                    sub_squares[index].add(board[i][j])
                
                if board[j][i] != '.':
                    if board[j][i] in col_nums:
                        return False
                    col_nums.add(board[j][i])

        return True