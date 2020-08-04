# Creating functions in python
# Generally functions in Python have can return a value.
# If a function doesnot return anything it will cause effect than returning anything.
# Try to write python functions which return a value and value its returned value is used someehre else than just printing somewhere.

# Python functions are declared using 'def' keyword.

def squareNumbers(x):
    if x is int:
        return x*x
    else:
        return "Input is not an integer!"


print("This is square of numbers")
print(squareNumbers(10))

# Create a sentence former using functions.
def ordinal(value):
    endRoot = str(value)
    if endRoot.endswith('1'):
        return "st"
    elif endRoot.endswith('2'):
        return "nd"
    elif endRoot.endswith('3'):
        return "rd"
    else :
        return "th"

def ordinalValue(value):
    return str(value) + ordinal(value)

print("Enter the number here!")
print(ordinalValue(input()))