#Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    chars = list(sentence)
    count = 0
    for char in chars:
        if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
            count += 1
    return count

print(get_count("aeiou"))
print(get_count("y"))
print(get_count("bcdfghjklmnpqrstvwxz y"))
print(get_count(""))
print(get_count("abracadabra"))
