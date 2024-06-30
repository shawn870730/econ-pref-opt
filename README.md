# Microeconomics Portfolio Optimization

## Overview

This project focuses on the optimization of financial portfolios, including the analysis and calculation of budget constraints, utility functions, and optimal asset allocations. It provides Python implementations for solving various problems related to microeconomics, specifically targeting portfolio management and optimization.

## Files

- **econ_pref_opt**: This Python script contains functions and plotting routines to solve portfolio optimization problems. The code includes calculations for budget constraints, plotting budget lines, finding optimal asset allocations, and visualizing changes in portfolio choices due to varying market conditions.

## Features

1. **Portfolio Valuation**: Calculate the value of an initial portfolio consisting of different assets.

2. **Budget Constraints**: Derive and plot budget constraints for different asset prices and initial holdings.

3. **Optimal Asset Holdings**: Compute the maximum holdings of assets that can be afforded under given budget constraints.

4. **Utility Functions**: Analyze different types of utility functions and their impact on portfolio choice. The utility functions considered include:
   - **Logarithmic Utility Function**: $ \U(x_1, x_2) = a \log(x_1) + b \log(x_2) \$
   - **Square Root Utility Function**: $ \U(x_1, x_2) = (x_1)^{1/2} + 2(x_2)^{1/2} $
   - **Exponential Utility Function**: $ U(x_1, x_2) = -\exp(-x_1) - \exp(-x_2) $
   - **Cobb-Douglas Utility Function**: $ U(x_1, x_2) = 2 \log(x_1) + 3 \log(x_2) $
   - **CRRA (Constant Relative Risk Aversion) Utility Function**: $ U(x_n) = \frac{(x_n)^{1-\theta}}{1-\theta} ,\  where\ \theta > 0 $
   - **CARA (Constant Absolute Risk Aversion) Utility Function**: $ U(x_n) = -\exp(-\alpha x_n) ,\  where \ \alpha > 0 $

5. **Marginal Utility Analysis**: Evaluate the marginal utility of a dollar spent on different assets and its role in optimal portfolio selection.

6. **Graphical Analysis**: Use `matplotlib` to plot budget constraints, optimal choices, and indifference curves for visualizing portfolio optimization.

7. **Comparative Statics**: Analyze how changes in asset prices and initial endowments affect the optimal portfolio choices.

## Budget Constraints

The budget constraints are derived based on the initial portfolio and prices of the assets. For example, if Murphy is trading crude oil and natural gas with prices $ p_1 $ and $ p_2 $ respectively, and his initial endowment is $ (e_1, e_2) $, the budget constraint can be written as:

$ p_1 x_1 + p_2 x_2 = p_1 e_1 + p_2 e_2 $

This budget constraint is then used to determine the maximum holdings of each asset and to plot the budget line, showing the feasible combinations of the assets that Murphy can afford.

## Requirements

- Python 3.x
- `numpy`
- `matplotlib`
- `scipy`
