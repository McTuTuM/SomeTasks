# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    arr2 = ["!",",",".","?"]
    temp_arr =[]
    z =' '
    arr = text.split()
    for i in range(len(arr)):
        if arr[i] not in arr2:
            temp = arr[i][0]
            arr[i] += temp
            a = arr[i][1:] + 'ay'
            temp_arr.append(a)
            z.join(a)
        else:
            temp_arr.append(arr[i])
    return " ".join(temp_arr)


print(pig_it('Hello world !'))    
#igPay atinlay siay oolcay 

# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])