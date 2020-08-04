a = None
print(a is not None)  # None is a optional datatype to just like nil in any other programming language.


# IF Statements
if a == 10 : 
    print("A is Equal to 10")
else :
    print("A is None")

# Creating a infinite loop
# while True:
#     print("This is an Infinite loop")

# Creating a infinite while loop with the user input
while True:
    response = input()
    if int(response) % 7 == 0:
        print("Number is divisible by 7")
        break
    else:
        print("This is not divisible by 7")



