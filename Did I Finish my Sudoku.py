# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter.
# If the board is valid return 'Finished!', otherwise return 'Try again!'
def done_or_not(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if len(set(tuple(board[i]))) == 9:
                print('Frue')
            if len(set(board[j])) == 9:
                print("Frue")


print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                    ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
                    # 'Try again!');)