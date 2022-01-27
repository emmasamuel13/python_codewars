#Given an integral number, determine if it's a square number

def is_square(n):
    import math
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        root = math.sqrt(n)
        if root == int(root):
            return True
        else:
            return False

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))
