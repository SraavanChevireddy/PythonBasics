import numpy as np
import pandas as pd
import datetime

# Read the CSV list from the localpath. 
diseasesTable = pd.read_csv("/Users/sraavanchevireddy/Desktop/Machine Learning Datasets/symptoms/symptoms2.csv")
print(diseasesTable)

# Now, cluster the data with the symptoms alone as a numpy array.
diseasesList = np.array(pd.DataFrame(diseasesTable,columns=['name']))
print(diseasesList)

def greetingMessage():
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        print("Good Morning, Sraavan")
    else:
        print("Good Evening, Sraavan")
    print("How are you doing today?")
    whereAboutResponse = input()
    if whereAboutResponse is None:
        print("Huh! I'm smarter than you 😎")
    else:
        if "great" in str(whereAboutResponse):
            print("Great! What's your problem ?")
            userProblem = input()
            return str(userProblem)
        else:
            print("Oh Boy! Go get a life! 😊")
            return 10

def clusterDiseaseswith(userInput="I'm good!"):
    """ This function will search the diseases from the pd table of symptoms, match with the user input and returns the list of diseases he can get treated.
    
    Args: userInput is an optional parameter which fetches the results and binds it to a protocol data clusters in ln:6

    Returns: List of matched diseases ?
    """
    print("Anything!")
    while True:    
        print("Searching the diseases in the list")
        filteredResults = np.where(userInput in diseasesList)
        break


#Create a infinite loop with the user input
while True:
    if isinstance(greetingMessage(),str):
        #Get the diseases list and search it with the predefined model.
        filteredResults = np.where(greetingMessage() in diseasesList)
        print("These are the filtered results {0}",filteredResults)
        break
    elif greetingMessage() == 10:
        print("Program ended with non-zero exit code. 10")
        break
    else:
        print("Don't have any option left for me!")





            

