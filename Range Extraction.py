# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

# Example:

# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-6,-3-1,3-5,7-11,14,15,17-20"

# def solution(args):
#     flag = False
#     res = ""
#     st = 0
#     while not flag:
#         for i in range(st, len(args)):
#             if flag:
#                 break
#             j = i
#             cnt = 0
#             try:
#                 if args[i] + 1 == args[i + 1]:
#                     try:
#                         while args[j] + 1 == args[j + 1]:
#                             cnt += 1
#                             j += 1
#                         if cnt >= 2:
#                             res += str(args[i]) + "-" + str(args[i + cnt]) + ","
#                             st = i + cnt + 1
#                             break
#                         else:
#                             res += str(args[i]) + "," + str(args[i + cnt]) + ","
#                             st = i + cnt + 1
#                             break
#                     except IndexError:
#                         if cnt >= 2:
#                             res += str(args[i]) + "-" + str(args[i + cnt])
#                             flag = True
#                         else:
#                             res += str(args[i]) + "," + str(args[i + cnt]) 
#                             flag = True
#                 else: 
#                     res += str(args[i]) + "," 
#             except IndexError:
#                      res += str(args[i])
#                      flag = True
#     return res   
def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)
print(solution([-54, - 53, -50, -13, -12 ]))
#'-6,-3-1,3-5,7-11,14,15,17-20'


