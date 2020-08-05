# Lists are the collection of different objects in Python.
# We can use negative indices in list
# Negative index does not mean it have a `-1` index. -1 implies length minus 1th index.

listOfApples = ["Apple","Orange","Mango","Banana","Pine Apple"]
print(listOfApples[-1]) # Last but one

print(listOfApples[-2])#Last but second



# SLICING IN LIST
s = [3,186,4431,7440,10483]

print(s[1:3]) # [186,4431]
print(s[1:-1]) # [186,4431,7440]
print(s[2:]) # [4431,7440,10483]
print(s[:2]) # [3,186]

print(s[:]) # [3,186,4431,7440,10483]