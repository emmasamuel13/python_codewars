#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    digits = str(num)
    digits = list(digits)
    digits.sort()
    digits.reverse()
    large_number = [str(number) for number in digits]
    large_number = "".join(large_number)
    large_number = int(large_number)
    return large_number


print(descending_order(0))
print(descending_order(15))
print(descending_order(123456789))
