#You get an array of numbers, return the sum of all of the positives ones.
#Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    sum = 0
    for x in arr:
        if x > 0:
            sum = sum + x
    return sum


print(positive_sum([1,2,3,4,5]))
print(positive_sum([1,-2,3,4,5]))
print(positive_sum([-1,2,3,4,-5]))
