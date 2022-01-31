#Your task is to write a function that takes a string and return a new string with all vowels removed.

def disemvowel(string_):
    arr = list(string_)
    no_vowel = []
    for char in arr:
        if(char != "a" and char != "e" and char != "i" and char != "o" and char != "u" and char != "A" and char != "E" and char != "I" and char != "O" and char != "U"):
            no_vowel.append(char)
    return "".join(no_vowel)

print(disemvowel("This test is for losers LOL"))
