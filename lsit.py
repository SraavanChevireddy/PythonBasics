
# Lists are set in square brackets
# Items in the list are separated by commas.
listOne = [1,2,3]
listTwo = ["Apple","Mango","Pine Apple"]

print(listOne)
print(listTwo)

# List operations
# Append an element to list
listOne.append("Kiwi")

#Replace an element in the list
listTwo[2] = "Water melon!"

print("Please enter your input")
while True:
    element = input()
    if element is str:
        print("String found adding to list two")
        listTwo.append(element)
    elif element is int:
        print("Integer found adding to list one")
        listOne.append(element)
    else:
        print("Unidentified data type found. Try again. Exiting the commad!")
        break


for eachItem in listOne:
    print(eachItem)