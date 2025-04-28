# QMB6315: Python for Business Analytics
## Spring 2025

# Final Examination

##Enter the summary statistics from your recommended model in the code block below.

## Recommended model

```
Question 4f: Recommended Model (e.g., Full Model)
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              purchases   R-squared:                       0.583
Model:                            OLS   Adj. R-squared:                  0.576
Method:                 Least Squares   F-statistic:                     76.26
Date:                Thu, 24 Apr 2025   Prob (F-statistic):           2.07e-87
Time:                        11:14:01   Log-Likelihood:                -5003.5
No. Observations:                 500   AIC:                         1.003e+04
Df Residuals:                     490   BIC:                         1.007e+04
Df Model:                           9                                         
Covariance Type:            nonrobust                                         
=========================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------
Intercept             -3.286e+04   6549.112     -5.017      0.000   -4.57e+04      -2e+04
homeownership[T.Rent] -6526.8141    530.983    -12.292      0.000   -7570.099   -5483.529
income                   -0.0496      0.012     -3.966      0.000      -0.074      -0.025
credit_limit             -0.5489      0.152     -3.606      0.000      -0.848      -0.250
fico                     89.0137     13.734      6.481      0.000      62.028     115.999
num_late               2646.4521    214.530     12.336      0.000    2224.941    3067.963
past_def               1242.8911    826.098      1.505      0.133    -380.241    2866.023
num_bankruptcy         2122.7518    944.217      2.248      0.025     267.537    3977.966
avg_income               -0.0414      0.021     -1.944      0.052      -0.083       0.000
density                   3.5650      0.450      7.921      0.000       2.681       4.449
==============================================================================
Omnibus:                       46.505   Durbin-Watson:                   1.955
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               59.946
Skew:                           0.728   Prob(JB):                     9.61e-14
Kurtosis:                       3.871   Cond. No.                     2.45e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.45e+06. This might indicate that there are
strong multicollinearity or other numerical problems.
# Regression output goes here.

```