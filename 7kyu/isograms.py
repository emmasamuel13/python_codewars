#An isogram is a word that has no repeating letters, consecutive or non-consecutive.
#Implement a function that determines whether a string that contains only letters is an isogram.
#Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    string = string.lower()
    array = list(string)
    no_dup = list(dict.fromkeys(string))
    return array == no_dup

print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))
