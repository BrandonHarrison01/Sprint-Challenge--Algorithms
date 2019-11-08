'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    th = 0
    word = list(word)
    count = 0

    if word == []:
        return 0

    def recur(word):
        nonlocal count
        nonlocal th

        if count == len(word) - 1:
            print(th)   # <- when I change this line to return th it doesn't return anything
            
        else:
            print(count)
            if word[count] == 't' and word[count + 1] == 'h':
                th += 1
            count += 1
            recur(word)

    return recur(word)


print(count_th(''))
print(count_th('abcthxyz'))
print(count_th('abcthefthghith'))
print(count_th('thhtthht'))
print(count_th('THtHThth'))
