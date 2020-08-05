import csv
import pandas as pd

# Setup the dataframe for the Set.
df = pd.read_csv("/Users/sraavanchevireddy/Downloads/netflix_titles.csv")
print(df)  # This will return a matrix of the dataset.

# To select only few datasets.Use this key style
manipulatedData = pd.DataFrame(df, columns= ['show_id','type','title','country','date_added',])

print("This is the changed data for the selected labels")
print(manipulatedData)

# Get all movies in the list.
sampleMovieSpace = pd.DataFrame(manipulatedData,columns=['type'])



