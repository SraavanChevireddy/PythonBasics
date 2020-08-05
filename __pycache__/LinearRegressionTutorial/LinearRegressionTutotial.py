import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the CarDekho Sales report CSV from the Desktop Folder.
# -------- Check for the path of CSV While you are using this on your python navigator ----------

# In this tutorial we are creating a regression model to measure the kilometers driven and 
# Depreceated car value depending on the kilometers.

# Initialize the size of the plot graph
plt.rcParams['figure.figsize'] = (20.0,10.0)

# Reading Data
regressionData = pd.read_csv("/Users/sraavanchevireddy/Desktop/Machine Learning Datasets/33080-1320127-bundle-archive/car data.csv")

# Now frame the data from the binding varible using the column value.
carInformation = pd.DataFrame(regressionData,columns=['Present_Price','Kms_Driven'])
print(carInformation.shape)
print(carInformation.head)

# Now let's collect the x and y values.
x_axis = carInformation['Present_Price'].values
y_axis = carInformation['Kms_Driven'].values

print(x_axis)

# Now lets calculate the mean of X and Y values.
mean_x = np.mean(x_axis)
mean_y = np.mean(y_axis)

# Total number of values 
n = len(x_axis)

# Now, lets calculate the line equation for the linear regression.
numerator = 0
denominator = 0

for i in range(n):
    numerator += (x_axis[i] - mean_x) * (y_axis[i] - mean_y)
    denominator += (x_axis[i] - mean_x) ** 2


slope = numerator / denominator

# Remember the line equation for Linear regression y = mx + c
# Caluculate the 'c'. This is the y-intercept for the line.
x_intercept = mean_y - (slope*mean_x)

print("This is slope")
print(slope)

print("This is x intercept")
print(x_intercept)


# Now lets print these values on a regression line.
max_x = np.max(x_axis) + 100
min_x = np.min(x_axis) + 100

# Let's calculate the line values here.
x = np.linspace(min_x,max_x,1000)
y = slope*x + x_intercept # y = mx + c

# Lets plot a line
plt.plot(x,y,color='#58b970',label='Regression Label')

# Mark the scatter points
plt.scatter(x_axis,y_axis,c='#ef5423',label='Scatter Label')

plt.xlabel("Present Price")
plt.ylabel("Kilometers Driven")
plt.legend()
plt.show()





