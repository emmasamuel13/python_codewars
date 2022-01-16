#Write a function called repeatStr which repeats the given string string exactly n times.

def repeat_str(repeat, string):
    repeats = string * repeat
    return repeats

print(repeat_str(4, 'a'))
print(repeat_str(3, 'hello '))
print(repeat_str(2, 'abc'))
