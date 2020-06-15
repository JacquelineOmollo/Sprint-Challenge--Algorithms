'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case condition is the string empty
    if len(word) < 2:
        return 0
    # If the first character of the string is equal to the character taken from the user, the count is incremented.
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])

