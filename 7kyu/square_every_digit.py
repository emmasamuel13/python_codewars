#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

def square_digits(num):
    string = str(num)
    digits = list(string)
    squared = []
    for digit in digits:
        integer = int(digit)
        squared.append(integer ** 2)
    squared = [str(number) for number in squared]
    squared = "".join(squared)
    squared = int(squared)
    return squared

print(square_digits(9119))
print(square_digits(0))
