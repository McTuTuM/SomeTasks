# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter.
# If the board is valid return 'Finished!', otherwise return 'Try again!'
from traceback import print_tb


def done_or_not(board):
    cnt, cnt1, cnt2 = 0, 0, 0
    for i in range(len(board)):
    #     # for j in range(len(board)):
    #     #     if len(set(tuple(board[i]))) == 9:
    #     #         print('True')
        if len(set(tuple(board[i][j] for j in range(len(board))))) == 9:
            cnt += 1
            if cnt == 9:
                a = True 
            else: 
                a = False

        if len(set(tuple(board[j][i] for j in range(len(board))))) == 9:
            cnt1 += 1
            if cnt1 == 9:
                a1 = True
            else: 
                a1 = False
    for i in range(0, len(board),3):
        for j in range(0, len(board),3):
            if board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i][j + 1] +board[i][j + 2] + board[i + 1][j + 2] + board[i + 2][j + 1] == 45: 
                a2 = True
            else: 
                a2 = False
    print(a,a1,a2)
    if a and a1 and a2 == True:
        return "Finished!"
    else:
        return "Try again!"
# print(done_or_not(  [[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                     ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                     ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                     ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                     ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                     ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                     ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                     ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                     ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))
#                     # 'Finished!');)s
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])), 
                        # 'Try again!');


# import numpy as np
# def done_or_not(aboard): #board[i][j]
#   board = np.array(aboard)

#   rows = [board[i,:] for i in range(9)]
#   cols = [board[:,j] for j in range(9)]
#   sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
  
#   for view in np.vstack((rows,cols,sqrs)):
#       if len(np.unique(view)) != 9:
#           return 'Try again!'
  
#   return 'Finished!'