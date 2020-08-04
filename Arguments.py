
# Return Arguments
m  = [9,10,11,21,50]
def modify(k):
    m.append(k)
    print("k = ", k)
modify(10)

# Return statements with 
def replace(f):
    return f
c=0
c is replace(5)
print("This is the value of c ", c)

# Function arguments with default parameters
def makeBanner(message,banner="User"):
    print(message + banner)

# Calling a default parameter function using one parameter.
makeBanner("Welcome ")

#Calling a default parameter function using second parameter.
makeBanner("Welcome ","Sraavan")



class PersonA(): 
    def printSomething():
        print("Printing Something!")
    
    def printHelloWorld():
        print("Printing Hello World")

class PersonB():
    def printSomething():
        print("Printing something")

    def printHelloWorld():
        print("Printing Hello World")

 
PersonA().printHelloWorld


    
        

        
    