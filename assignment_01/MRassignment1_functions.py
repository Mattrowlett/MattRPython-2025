# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Matthew Rowlett
#
# Date:04/10/25
#
##################################################
#
# Sample Script for Assignment 1:
# Function Definitions
#
##################################################
"""

##################################################
# Part a) Variance
##################################################

def variance(x):
    """
    Calculates the variance of a list x.
    
    Some examples are given below but you need to add some 
    that result in the answers given.
    
    >>> variance([101, 103, 94, 102, 100])
    10.0
    >>> variance([99,101,99,101,99,101])
    1.0
    >>> variance([])
    0.0
    
    """
    if len(x) == 0:
        return 0.0
    
    
    n = len(x)  # Number of elements
    x_bar = sum(x) / n  # Mean of the list
    
    # Calculate variance: sum of squared differences from mean, divided by (n-1)
    if n == 1:
        return 0.0  # Avoid division by zero for single element
       
    var = sum((xi - x_bar) ** 2 for xi in x) / (n)   
    
    
    return var


##################################################
# Part b) Covariance
##################################################

def covariance(y, x):
    """
    Calculates the covariance of two lists y and x.
    
    Some examples are given below but you need to add some 
    that result in the answers given.
    
    >>> covariance([99,101,99,101,99,101], \
                   [99,101,99,101,99,101])
    1.0
    >>> covariance([], [])
    -2.0
    >>> covariance([], \
                   [])
    0.0
    
    """
    
    if len(x) == 0 or len(y) == 0:
        return 0.0  # Adjust based on expected output; -2.0 seems incorrect
    
    n = len(x)  # Number of elements (assume x and y have same length)
    x_bar = sum(x) / n  # Mean of x
    y_bar = sum(y) / n  # Mean of y
    
    # Calculate covariance
    if n == 1:
        return 0.0  # Avoid division by zero
    covar = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, y)) / (n - 1)
    
        
    return covar



##################################################
# Part c) Slope Coefficient
##################################################

def ols_slope(y, x):
    """
    Calculates the slope coefficient 
    by ordinary least squares
    for the linear regression model 
    between two lists y and x.
    
    >>> ols_slope([2, 2, -2, -2], [-1, -1, 1, 1])
    -2.0
    >>> ols_slope([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100])
    2.0
    >>> ols_slope([99,101,99,101,99,101], \
                  [99,101,99,101,99,101])
    1.0
    """
    
    covar = covariance(y, x)
    var = variance(x)
    
    if var == 0:
        return 0.0
    slope = covar / var
    
    return slope
    
    
 
  
    
    return slope


##################################################
# Part d) Intercept
##################################################

def ols_intercept(y, x, beta_1_hat):
    """
    Calculates the intercept coefficient 
    by ordinary least squares
    for the linear regesssion model 
    between two lists y and x.
    
    The examples are given below but you need to fill in the answers.
    
    >>> ols_intercept([2, 2, -2, -2], [-1, -1, 1, 1], -2.0)
    0.0
    >>> ols_intercept([102, 106, 88, 104, 100], \
                  [101, 103, 94, 102, 100], 2.0)
    -100
    >>> ols_intercept([99,101,99,101,99,101], \
                  [99,101,99,101,99,101], 1.0)
    0.0
    
    """
    
    n = len(y)
    if n == 0:
        return 0.0
    x_bar = sum(x) / n
    y_bar = sum(y) / n
    
    intercept = y_bar - beta_1_hat * x_bar
    return intercept 
    

##################################################
# Part e) Sum of Squared Residuals
##################################################

    def ssr(y, x, beta_0, beta_1):
        """
    Calculates the sum of squared residuals for 
    the bivariate linear regression model.
    
    >>> ssr([2, 2, 2], [1, 1, 1], 0.5, 0.5)
    3.0
    >>> ssr([3, 0, 3], [0, 2, 2], 1.0, 0.5)
    9.0
    >>> ssr([2, 3, 4], [1, 2, 3], 1.0, 1.0)
    0.0
    """
        ssr = sum((yi - (beta_0 + beta_1 * xi)) ** 2 for yi, xi in zip(y, x))
        return ssr






##################################################
# End
##################################################
