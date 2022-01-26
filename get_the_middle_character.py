#You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character.
#If the word's length is even, return the middle 2 characters.

def get_middle(s):
    letters = list(s)
    length = len(letters)
    middle = []
    mid = int(length / 2)
    if length % 2 == 0:
        middle.extend((letters[mid - 1], letters[mid]))
    else:
        middle.append(letters[mid])
    return "".join(middle)

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))
