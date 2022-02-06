#Check to see if a string has the same amount of 'x's and 'o's.
#The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    s = s.lower()
    letters = list(s)
    x_and_o = 0
    for letter in letters:
        if letter == "x":
            x_and_o += 1
        elif letter == "o":
            x_and_o -= 1
    return x_and_o == 0

print(xo('xo'))
print(xo('xo0'))
print(xo('xxxoo'))
