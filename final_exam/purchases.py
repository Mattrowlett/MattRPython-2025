# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Matt Rowlett
#
# Date: 4/24/2025
#
##################################################
#
# Sample Script for Final Examination:
# Obtaining Data from a Database
# and Building Predictive Models
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import os

##################################################
# Set up Workspace
##################################################

import sqlite3
import pandas as pd
import statsmodels.formula.api as smf
import math
import numpy as np

##################################################
# Question 1: Connect to a Database
#     and Obtain Applications Data
##################################################

#--------------------------------------------------
# a. Connect to the database called customers.db
#     and obtain a cursor object.
#--------------------------------------------------

# Connect to the database and create a cursor 

conn = sqlite3.connect(r"C:\Users\Matt Rowlett\OneDrive - University of Central Florida\Desktop\GitHub QMB6315 Python\MattRPython-2025\final_exam\customers.db")
cur = conn.cursor()

# Verify table schemas (optional, comment out after checking)
print("Applications schema:", cur.execute("PRAGMA table_info(Applications)").fetchall())
print("CreditBureau schema:", cur.execute("PRAGMA table_info(CreditBureau)").fetchall())
print("Demographic schema:", cur.execute("PRAGMA table_info(Demographic)").fetchall())

# Question 1a: SQL query to obtain data from Applications table

query_1 = "SELECT * FROM Applications"

#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------
# Question 1b: Store data in DataFrame purchase_app

print(query_1)
cur.execute(query_1)

# Fetch all rows and create DataFrame with column names

columns = [desc[0] for desc in cur.description]
purchase_app = pd.DataFrame(cur.fetchall(), columns=columns)

# Describe the contents of the dataframe to check the result (optional)
print("Question 1b: DataFrame Description")
print(purchase_app.describe())
print("Question 1b: DataFrame Columns")
print(purchase_app.columns)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

# Question 1c: Estimate regression model

reg_model_app = smf.ols('purchases ~ income + homeownership + credit_limit', data=purchase_app).fit()
print("Question 1c: Regression Model for Applications")
print(reg_model_app.summary())

# Could use a loop with a pd.concat() command.

# Describe the contents of the dataframe to check the result.
purchase_app.describe()
purchase_app.columns


#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_app_check = smf.ols('purchases ~ income + homeownership + credit_limit', data=purchase_app).fit()
print("Question 1c: Regression Model to Check Progress")

# Display a summary table of regression results.
print(reg_model_app_check.summary())


##################################################
# Question 2: Obtain CreditBureau Data
##################################################

#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data.
#--------------------------------------------------

query_app_bureau = """
SELECT a.*, b.fico, b.num_late, b.past_def, b.num_bankruptcy
FROM Applications a
LEFT JOIN CreditBureau b ON a.ssn = b.ssn
"""

#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

print(query_app_bureau)
cur.execute(query_app_bureau)

# Fetch all rows and create DataFrame with column names

columns = [desc[0] for desc in cur.description]
purch_app_bureau = pd.DataFrame(cur.fetchall(), columns=columns)


# Could use a loop with a pd.concat() command.

# Describe the contents of the dataframe to check the result.

print("Question 2b: DataFrame Description")
print(purch_app_bureau.describe())
print("Question 2b: DataFrame Columns")
print(purch_app_bureau.columns)

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

# Question 2c: Estimate regression model
reg_model_app_bureau = smf.ols('purchases ~ income + homeownership + credit_limit + fico + num_late + past_def + num_bankruptcy', data=purch_app_bureau).fit()
print("Question 2c: Regression Model for Applications + CreditBureau")

# Display a summary table of regression results.
print(reg_model_app_bureau.summary())


##################################################
# Question 3: Obtain Demographic Data
##################################################


#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data.
#    and then joined with the Demographic data.
#--------------------------------------------------

# Question 3a: SQL query to join Applications, CreditBureau, and Demographic tables

query_full = """
SELECT a.*, b.fico, b.num_late, b.past_def, b.num_bankruptcy, d.avg_income, d.density
FROM Applications a
LEFT JOIN CreditBureau b ON a.ssn = b.ssn
LEFT JOIN Demographic d ON a.zip_code = d.zip_code
"""

# Question 3b: Store data in DataFrame purchase_full
print("Question 3a: SQL Query")
print(query_full)
cur.execute(query_full)

#--------------------------------------------------
# b. Create a data frame and load the query.
#--------------------------------------------------

columns = [desc[0] for desc in cur.description]
purchase_full = pd.DataFrame(cur.fetchall(), columns=columns)

# Could use a loop with a pd.concat() command.

# Check to see the columns in the result.

print("Question 3b: DataFrame Description")
print(purchase_full.describe())
print("Question 3b: DataFrame Columns")
print(purchase_full.columns)


#--------------------------------------------------
# c. Fit another regression model.
#--------------------------------------------------

reg_model_full = smf.ols('purchases ~ income + homeownership + credit_limit + fico + num_late + past_def + num_bankruptcy + avg_income + density', data=purchase_full).fit()
print("Question 3c: Regression Model for All Tables")

# Display a summary table of regression results.
print(reg_model_full.summary())


##################################################
# Question 4: Advanced Regression Modeling
##################################################

#--------------------------------------------------
# Parts a-c with utilization.
#--------------------------------------------------


# Question 4a: Create a variable for credit utilization.
purchase_full['utilization'] = purchase_full['purchases'] / purchase_full['credit_limit']

# Question 4b: Describe utilization
print("Question 4b: Description of Utilization")
print(purchase_full['utilization'].describe())

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

# Question 4c: Regression model for utilization
reg_model_util = smf.ols('utilization ~ income + homeownership + fico + num_late + past_def + num_bankruptcy + avg_income + density', data=purchase_full).fit()
print("Question 4c: Regression Model for Utilization")
print(reg_model_util.summary())


#--------------------------------------------------
# Parts d-f with log_odds_util.
#--------------------------------------------------


# Question 4d: Create a variable for credit utilization.
purchase_full['log_odds_util'] = purchase_full['utilization'].apply(lambda x: math.log(x / (1 - x)) if 0 < x < 1 else np.nan)


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


# Question 4e: Regression model for log_odds_util
reg_model_log_odds = smf.ols('log_odds_util ~ income + homeownership + fico + num_late + past_def + num_bankruptcy + avg_income + density', data=purchase_full).fit()
print("Question 4e: Regression Model for Log-Odds Utilization")
print(reg_model_log_odds.summary())

# Question 4f: Recommend the best model
print("Question 4f: Recommended Model (e.g., Full Model)")
print(reg_model_full.summary())

# Close database connection
cur.close()
conn.close()


##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
#conn.commit()
# No changes were necessary -- only reading.

# Close the connection when finished. 
#conn.close()

# Then we can continue with this file when you have time
# to work on it later.



##################################################
# Extra code snippets
##################################################

# In case things go wrong, you can always drop the table
# and start over:
# cur.execute('DROP TABLE Applications')
# cur.execute('DROP TABLE CreditBureau')
# cur.execute('DROP TABLE Demographic')

# This can get the schema of the table,
# cur.execute("PRAGMA table_info('Applications')").fetchall()
# cur.execute("PRAGMA table_info('CreditBureau')").fetchall()
# cur.execute("PRAGMA table_info('Demographic')").fetchall()
# which states the names of the variables and the data types.


##################################################
# End
##################################################