#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if(number % 2 == 0):
        return("Even")
    else:
        return("Odd")


print(even_or_odd(2))
print(even_or_odd(1))
print(even_or_odd(0))
print(even_or_odd(1545452))
print(even_or_odd(7))
print(even_or_odd(78))
print(even_or_odd(17))
print(even_or_odd(74156741))
print(even_or_odd(100000))
print(even_or_odd(-123))
print(even_or_odd(-456))
