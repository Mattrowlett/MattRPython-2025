# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Matthew Rowlett
#
# Date: 04/10/2025
#
##################################################
#
# Sample Script for Assignment 2:
# Manipulating Data
#
##################################################
"""

##################################################
# Import Required Modules
################################################

import pandas as pd
import os


# Import a module for estimating regression models.
import statsmodels.formula.api as smf # Another way to estimate linear regression

##################################################
# Set up Workspace
##################################################


# Find out the current directory.
os.getcwd()

# Get the path where you saved this script.
# This only works when you run the entire script (with the green "Play" button or F5 key).
print(os.path.dirname(os.path.realpath(__file__)))
# It might be comverted to lower case, but it gives you an idea of the text of the path. 
# You could copy it directly or type it yourself, using your spelling conventions. 

# Change to a new directory.

# You could set it directly from the location of this file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Check that the change was successful.
os.getcwd()
# I got lower case output, even though my folders have some upper case letters.
# But anyway, it works.


##################################################
# Part a) Read Spreadsheet and Sales Data
##################################################

airplane_sales = pd.read_excel('airplane_data.xlsx', sheet_name='airplane_sales')
excel_file = pd.ExcelFile('airplane_data.xlsx')
print(excel_file.sheet_names)
print("Question 1b: Summary of airplane_sales")
print(airplane_sales.describe())

#--------------------------------------------------
# Fit a regression model.
#--------------------------------------------------
reg_model_sales = smf.ols('price ~ age', data=airplane_sales).fit()
print("\nQuestion 1c: Regression model price ~ age")
print(reg_model_sales.summary())



##################################################
# Part b) Read Specification Data
##################################################
# b) Summary of the data
airplane_specs = pd.read_excel('airplane_data.xlsx', sheet_name='airplane_specs')

#--------------------------------------------------
# Join the two datasets together.
#--------------------------------------------------
airplane_sales_specs = pd.merge(airplane_sales, airplane_specs, on='sale_id', how='inner')
print("\nQuestion 2c: Summary of airplane_sales_specs")
print(airplane_sales_specs.describe())


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------
reg_model_sales_specs = smf.ols('price ~ age + passengers + wtop + fixgear + tdrag', 
                                data=airplane_sales_specs).fit()
print("\nQuestion 2d: Regression model price ~ age + passengers + wtop + fixgear + tdrag")
print(reg_model_sales_specs.summary())

##################################################
# Part c) Read Performance Data
##################################################
airplane_perf = pd.read_excel('airplane_data.xlsx', sheet_name='airplane_perf')

#--------------------------------------------------
# Join the third dataset to the first two.
#--------------------------------------------------

airplane_full = pd.merge(airplane_sales_specs, airplane_perf, on='sale_id', how='inner')
print("\nQuestion 3c: Summary of airplane_full")
print(airplane_full.describe())

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = smf.ols('price ~ age + passengers + wtop + fixgear + tdrag + horse + fuel + ceiling + cruise', 
                         data=airplane_full).fit()
print("\nQuestion 3d: Regression model price ~ age + passengers + wtop + fixgear + tdrag + horse + fuel + ceiling + cruise")
print(reg_model_full.summary())


##################################################
# End
##################################################
