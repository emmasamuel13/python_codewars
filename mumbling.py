#This time no story, no theory. The examples below show you how to write function accum:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

def accum(s):
    s.lower()
    letters = list(s)
    mumble = []
    for letter in letters:
        times = letters.index(letter)
        times = times + 1
        mumbled = letter * times
        mumble.append(mumbled.capitalize())
    return "-".join(mumble)

print(accum("ZpglnRxqenU"))
print(accum("NyffsGeyylB"))
print(accum("MjtkuBovqrU"))
print(accum("EvidjUnokmM"))
print(accum("HbideVbxncC"))
