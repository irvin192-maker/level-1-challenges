def longest(arr):
    l_word = max(arr, key=len)
    for word in arr:
        if len(l_word) == len(word):
            print(word)
    return












