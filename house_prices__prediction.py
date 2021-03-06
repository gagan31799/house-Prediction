# -*- coding: utf-8 -*-
"""House_prices_ prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1klARNW_fOtYXt8eBl4G9b-qcIofRFV2j

# Capstone Project 16: House Price Prediction

---

### Context

The price of the house depends on various factors like locality, connectivity, number of rooms, etc. Change in the mindset of the millennial generation also contributes to ups and down in house prices as the young generation is much into renting than to owe a house. Predicting the right price of the house is important for investors in the real estate business. This makes it very important to come up with proper and smart technique to estimate the true price of the house.

### Problem Statement


You are willing to sell your house. You are not sure about the price of your house and want to estimate its price. You are provided with the dataset and need to make a prediction model which will help you to get a good estimate of your house for selling it.

---

### Data Description

The **housing** dataset contains the prices and other attributes. There are $545$ rows and $12$ attributes (features) with a target column (price). 

Following are the features:  

|Column|Description|
|---:|:---|
|`Price`|Price in INR|
|`area`|Area in square ft.|
|`bedrooms`|Number of bedrooms in the house|
|`bathrooms`|Number of bathrooms in the house|
|`stories`|Number of stores in the house|
|`mainroad`|Whether house is on main road or not(binary)|
|`guestroom`|Whether house have guestroom or not(binary)|
|`basement`|Whether house have basement or not(binary)|
|`airconditioning`|Whether house have airconditioning or not(binary)|
|`hotwaterheating`|Whether house have hotwaterheating or not(binary)|
|`parking`|Number of parking area|
|`prefarea`|Whether house have prefarea or not(binary)|
|`furnishingstatus`|Furnish status of the house|


  **Dataset Link:**  https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/house-prices.csv

---

### Things To Do

1. Explore the Housing dataset by creating the following plots:
   - Box plots between each categorical feature and the `price`.
   - Scatter plots between the numerical features and the `price`.
   
2. Convert categorical attributes into numerical attributes using feature encoding.

3. Build a linear regression model by selecting the most relevant features to predict the price of houses.

4. Evaluate the linear regression model by calculating the parameters such as coefficient of determination, MAE, MSE, RMSE, mean of residuals and by checking for homoscedasticity.

---

#### 1. Import Modules and Load Dataset

**Dataset Link:** https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/house-prices.csv
"""

# Import the required modules and load the dataset.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/house-prices.csv")
df.head(5)

# Get the information on DataFrame.
df.info()

# Check if there are any NULL values.
df.isna().sum()

"""---

#### 2. Exploratory Data Analysis

We need to predict the value of `price` variable, using other variables. Thus, `price` is the target or dependent variable and other columns except `price` are the features or the independent variables. 

Perform the following tasks:

- Create Box plots between each **categorical** variable and the target variable `price` to sense the distribution of values.

- Create the Scatter plots between each **numerical** variable and the target variable `price`. Determine which variable(s) shows linear relationship with the target variable `price`. 

- Create a normal distribution curve for the `price`.
"""

# Check categorical attributes
df_cat=df.select_dtypes(['object'])
df_cat.head()

# Boxplot for 'mainroad' vs 'price'
plt.figure(figsize=[15,5])
sns.boxplot(x='mainroad',y='price',data=df)
plt.show()

# Boxplot for 'guestroom' vs 'price'

plt.figure(figsize=[15,5])
sns.boxplot(x='guestroom',y='price',data=df)
plt.show()

# Boxplot for 'basement' vs 'price'
plt.figure(figsize=[15,5])
sns.boxplot(x='basement',y='price',data=df)
plt.show()

# Boxplot for 'hotwaterheating' vs 'price'
plt.figure(figsize=[15,5])
sns.boxplot(x='hotwaterheating',y='price',data=df)
plt.show()

# Boxplot for 'airconditioning' vs 'price'
plt.figure(figsize=[15,5])
sns.boxplot(x='airconditioning',y='price',data=df)
plt.show()

# Boxplot for 'prefarea' vs 'price'


plt.figure(figsize=[15,5])
sns.boxplot(x='prefarea',y='price',data=df)
plt.show()

# Boxplot for 'furnishingstatus' vs 'price'
plt.figure(figsize=[15,5])
sns.boxplot(x='furnishingstatus',y='price',data=df)
plt.show()

# Create scatter plot with 'area' on X-axis and 'price' on Y-axis

plt.figure(figsize=(15,4))
plt.scatter(df['area'],df['price'])
plt.title('Scatter plot with area on X-axis and price on Y-axis')
plt.xlabel('area')
plt.ylabel('Price')
plt.show()

# Create scatter plot with 'bedrooms' on X-axis and 'price' on Y-axis
plt.figure(figsize=(15,4))
plt.scatter(df['bedrooms'],df['price'])
plt.title('Scatter plot with bedrooms on X-axis and price on Y-axis')
plt.xlabel('bedrooms')
plt.ylabel('Price')
plt.show()

# Create scatter plot with 'bathrooms' on X-axis and 'price' on Y-axis
plt.figure(figsize=(15,4))
plt.scatter(df['bathrooms'],df['price'])
plt.title('Scatter plot with bathrooms on X-axis and price on Y-axis')
plt.xlabel('bathrooms')
plt.ylabel('Price')
plt.show()

# Create scatter plot with 'stories' on X-axis and 'price' on Y-axis
plt.figure(figsize=(15,4))
plt.scatter(df['stories'],df['price'])
plt.title('Scatter plot with stories on X-axis and price on Y-axis')
plt.xlabel('stories')
plt.ylabel('Price')
plt.show()

# Create a normal distribution curve for the 'price'.

# Create a probablity density function for plotting the normal distribution
def prob_density_func(series):
  CONST = 1 / (series.std() * np.sqrt(2 * np.pi))
  power_of_e = - (series - series.mean()) ** 2 / (2 * series.var()) # 'pd.Series.var()' function returns the variance of the series.
  new_array = CONST * np.exp(power_of_e)
  return new_array


# Plot the normal distribution curve using plt.scatter()
print(df['price'].mean())
plt.figure(figsize=[15,5])
plt.scatter(df['price'],prob_density_func(df['price']))
plt.title('Normal Distribution Curve for Price')
plt.legend()
plt.show()

"""---

#### 3. Feature encoding 

Perform feature encoding using `map()` function and one-hot encoding.
"""

# Replace yes with 1 and no with 0 for all the values in features 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea' using map() function.

a=['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
def binary_map(x):
  return x.map({'yes':1,'no':0})
df[a]=df[a].apply(binary_map)

# Print dataframe
df.head()

# Perform one hot encoding for furnishingstatus feature.
df_dummies=pd.get_dummies(df['furnishingstatus'],drop_first=False)
df=pd.concat([df,df_dummies],axis=1)
df.head()

# Drop 'furnishingstatus' feature
df.drop(columns=['furnishingstatus'],axis=1,inplace=True)

# Print dataframe 
df.head()

"""---

#### 4. Model Building and Evaluation 

Build a multiple linear regression model using the `statsmodels.api` module.
"""

# Split the 'df' Dataframe into the train and test sets.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Split the DataFrame into the train and test sets such that test set has 33% of the values.

train_df, test_df = train_test_split(df, test_size = 0.4, random_state = 42)

# Create separate data-frames for the feature and target variables for both the train and test sets.
features=list(df.columns.values)
features.remove('price')
#print(features)
X_train=train_df[features]
y_train=train_df['price']

X_test=test_df[features]
y_test=test_df['price']

# Build a linear regression model using all the features to predict prices.
import statsmodels.api as sm

X_train_sm = sm.add_constant(X_train)
# Fit the regression line using 'OLS'
#print(X_train_sm.info())
lr = sm.OLS(y_train, X_train_sm).fit()
# Print the parameters, i.e. the intercept and the slope of the regression line fitted
lr.params

# Print the summary of the linear regression report.
print(lr.summary())

# Calculate N and p values
n=X_train.shape[0]
p=X_train.shape[1]

print("number of Rows(N)= ",n,"\nNumber of Predictors(p)= ",p)

# Calculate the adjusted R-square value.
lr.rsquared_adj

"""**Q:** What is the Adjusted $R^2$ value?

**A:** 0.645

---

#### 5. Model Evaluation

Build a multiple linear regression model  using `sklearn` module. Also, evaluate the model by calculating $R^2$, MSE, RMSE, and MAE values.
"""

# Build multiple linear regression model using all the features

from sklearn.linear_model import LinearRegression

# Print the value of the intercept 

sklearn_lin_reg = LinearRegression()
sklearn_lin_reg.fit(X_train, y_train)

print("\nConstant".ljust(15, " "), f"{sklearn_lin_reg.intercept_:.6f}") 

# Print the names of the features along with the values of their corresponding coefficients.
for item in list(zip(X_train.columns.values, sklearn_lin_reg.coef_)):
  print(f"{item[0]}".ljust(15, " "), f"{item[1]:.6f}")

# Evaluate the linear regression model using the 'r2_score', 'mean_squared_error' & 'mean_absolute_error' functions of the 'sklearn' module.
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
y_test_pred = sklearn_lin_reg.predict(X_test)
y_train_pred = sklearn_lin_reg.predict(X_train)

print(f"\n\nTrain Set\n{'-' * 50}")
print(f"R-squared: {r2_score(y_train, y_train_pred):.6f}")
print(f"Mean Squared Error: {mean_squared_error(y_train, y_train_pred):.3f}")
print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_train, y_train_pred)):.3f}")
print(f"Mean Absolute Error: {mean_absolute_error(y_train, y_train_pred):.3f}")


print(f"\n\nTest Set\n{'-' * 50}")
print(f"R-squared: {r2_score(y_test, y_test_pred):.3f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_test_pred):.3f}")
print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_test, y_test_pred)):.3f}")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_test_pred):.3f}")

"""**Q:** What is the $R^2$ value for train set and test set?

**R-squared** (Train Set)=0.659<br>**R-squared**(Test Set)= 0.675

---

#### 6. Recursive Feature Elimination

Find out the best features out of all features using RFE and evaluate the model again.
"""

# Create a Python dictionary storing the moderately to highly correlated features with price and the corresponding correlation values.
# Keep correlation threshold to be 0.2

major_features={}

for i in features:
  coeff=np.corrcoef(df['price'],df[i])[0,1]
  if((coeff>=0.2) or(coeff<=-0.2)):
    major_features[i]=coeff
print("number of features moderately to highly correlated features with price: ",len(major_features))
major_features

# Perform RFE and select best 7 features  
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression


skl_lin_reg = LinearRegression()
rfe1 = RFE(skl_lin_reg, n_features_to_select=7)

rfe1.fit(X_train[major_features.keys()], y_train)

# Print the attributes.
print(major_features.keys(), "\n") 
print(rfe1.support_, "\n")    
print(rfe1.ranking_)

# Print the 7 features selected by RFE in the previous step.
rfe_features= X_train[major_features.keys()].columns[rfe1.support_]
rfe_features

# Build multiple linear regression model using all the features selected after RFE

# Split the DataFrame into the train and test sets such that test set has 33% of the values.

train_df, test_df = train_test_split(df, test_size = 0.33, random_state = 42)

X_train=train_df[rfe_features]
y_train=train_df['price']

X_test=test_df[rfe_features]
y_test=test_df['price']

# Build linear regression model using the 'sklearn.linear_model' module.

from sklearn.linear_model import LinearRegression

# Print the value of the intercept 

sklearn_lin_reg = LinearRegression()
sklearn_lin_reg.fit(X_train, y_train)

print("\nConstant".ljust(15, " "), f"{sklearn_lin_reg.intercept_:.6f}") 

# Print the names of the features along with the values of their corresponding coefficients.
for item in list(zip(X_train.columns.values, sklearn_lin_reg.coef_)):
  print(f"{item[0]}".ljust(15, " "), f"{item[1]:.6f}")

# Evaluate the linear regression model using the 'r2_score', 'mean_squared_error' & 'mean_absolute_error' functions of the 'sklearn' module.

from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
y_test_pred = sklearn_lin_reg.predict(X_test)
y_train_pred = sklearn_lin_reg.predict(X_train)

print(f"\n\nTrain Set\n{'-' * 50}")
print(f"R-squared: {r2_score(y_train, y_train_pred):.6f}")
print(f"Mean Squared Error: {mean_squared_error(y_train, y_train_pred):.3f}")
print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_train, y_train_pred)):.3f}")
print(f"Mean Absolute Error: {mean_absolute_error(y_train, y_train_pred):.3f}")


print(f"\n\nTest Set\n{'-' * 50}")
print(f"R-squared: {r2_score(y_test, y_test_pred):.3f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_test_pred):.3f}")
print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y_test, y_test_pred)):.3f}")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_test_pred):.3f}")

"""---

#### 7. Residual (Error) Analysis

Perform residual analysis to check if the residuals (errors) are normally distributed or not. For this, plot the  histogram of the residuals.
"""

# Create a histogram for the errors obtained in the predicted values for the train set.
train_residuals = y_train - y_train_pred
print(f"Mean of residuals = {np.mean(train_residuals):.3f}\n")

plt.figure(figsize = (15, 6))
sns.distplot(train_residuals, bins = 'sturges', label = f"Mean of residuals = {np.mean(train_residuals):.3f}\n")
plt.axvline(x = np.mean(train_residuals), color = 'red')
plt.legend()
plt.show()

# Create a histogram for the errors obtained in the predicted values for the test set.
test_residuals = y_test - y_test_pred
print(f"Mean of residuals = {np.mean(test_residuals):.3f}\n")

plt.figure(figsize = (15, 6))
sns.distplot(test_residuals, bins = 'sturges', label = f"Mean of residuals = {np.mean(test_residuals):.3f}\n")
plt.axvline(x = np.mean(test_residuals), color = 'red')
plt.legend()
plt.show()

"""---

#### 8. Verify Homoscedasticity 

Check for Homoscedasticity (constant variance) by creating a scatter plot between the errors and the target variable. Determine whether there is some kind of relationship between the error and the target variable.
"""

# Create a scatter plot between the errors and the dependent variable for the train set.

plt.figure(figsize = (15, 6))
plt.scatter(y_train,train_residuals)
plt.axhline(y = np.mean(train_residuals), color = 'red',label = f"Mean of residuals = {np.mean(train_residuals):.3f}\n")

plt.legend()
plt.show()