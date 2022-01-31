#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number
#Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    nums = numbers.split(" ")
    nums = list(map(int, nums))
    nums.sort()
    return "{} {}".format(nums[-1], nums[0])

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
print(high_and_low("1 2 3"))
