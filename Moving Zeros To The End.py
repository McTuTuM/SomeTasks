def move_zeros(array):
    ind = 0
    n = 0
    if len(array) == 0:
        return [] 
    for i in array:
        if i == 0:
            for j in range(ind + 1, len(array)):
                if array[j] != 0:
                    array[ind] = array.pop(j)
                    array.append(0)
                    n += 1
                    break
        ind += 1
        if  n + ind >= len(array) - 1:
            return array


move_zeros(
        [])
        # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])




# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))

# def move_zeros(array):
#     return sorted(array, key=lambda x: x==0 and type(x) is not bool)