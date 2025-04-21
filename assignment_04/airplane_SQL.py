# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Matthew Rowlett
#
# Date: 04/21/2025
#
##################################################
#
# Assignment 4:
# airplanes database
#
##################################################
"""

import sqlite3
import pandas as pd
import os
# Import a module for estimating regression models.
import statsmodels.formula.api as smf  # Another way to estimate linear regression

# Ensure the database file exists
db_path = 'airplanes.db'
if not os.path.exists(db_path):
    raise FileNotFoundError(f"Database file {db_path} not found in the current directory.")

# Connect to the database
conn = sqlite3.connect(db_path)

# Question 1: Regression Model Using Sales Table
# a) Query to obtain data from Sales table
query_sales = "SELECT sale_id, age, price FROM Sales;"

# b) Load data into DataFrame
airplane_sales = pd.read_sql_query(query_sales, conn)

# c) Estimate regression model (price ~ age)
reg_model_sales = smf.ols('price ~ age', data=airplane_sales).fit()
print("Question 1c: Regression Model Summary (Sales)")
print(reg_model_sales.summary())

# Question 2: Regression Model Using Sales and Specs Tables
# a) Query to join Sales and Specs tables
query_sales_specs = """
SELECT s.sale_id, s.age, s.price, sp.passengers, sp.wtop, sp.fixgear, sp.tdrag
FROM Sales s
LEFT JOIN Specs sp ON s.sale_id = sp.sale_id;
"""

# b) Load data into DataFrame
airplane_sales_specs = pd.read_sql_query(query_sales_specs, conn)

# c) Estimate regression model (price ~ age + pass + wtop + fixgear + tdrag)
reg_model_sales_specs = smf.ols('price ~ age + passengers + wtop + fixgear + tdrag',
                                data=airplane_sales_specs).fit()
print("\nQuestion 2c: Regression Model Summary (Sales + Specs)")
print(reg_model_sales_specs.summary())

# Question 3: Regression Model Using Sales, Specs, and Perf Tables
# a) Query to join Sales, Specs, and Perf tables
query_full = """
SELECT s.sale_id, s.age, s.price, sp.passengers, sp.wtop, sp.fixgear, sp.tdrag,
       p.horse, p.fuel, p.ceiling, p.cruise
FROM Sales s
LEFT JOIN Specs sp ON s.sale_id = sp.sale_id
LEFT JOIN Perf p ON s.sale_id = p.sale_id;
"""

# b) Load data into DataFrame
airplane_full = pd.read_sql_query(query_full, conn)

# c) Estimate regression model (price ~ all variables)
reg_model_full = smf.ols('price ~ age + passengers + wtop + fixgear + tdrag + horse + fuel + ceiling + cruise',
                         data=airplane_full).fit()
print("\nQuestion 3c: Regression Model Summary (Sales + Specs + Perf)")
print(reg_model_full.summary())

# Close the database connection
conn.close()