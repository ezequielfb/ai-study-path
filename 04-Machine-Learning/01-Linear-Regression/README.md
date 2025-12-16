# Project: Salary Prediction with Linear Regression

## Overview
This is my first Machine Learning implementation using **Scikit-Learn**. The goal was to understand the fundamental workflow of a Supervised Learning model.
I created a simple dataset to predict a person's salary based on their age using a **Linear Regression** algorithm.

## Technologies & Libraries
- **Python 3.x**
- **Pandas:** Data manipulation and DataFrame creation.
- **Scikit-Learn:** Model creation (LinearRegression), data splitting, and metrics (MAE).
- **Matplotlib:** Data visualization (Scatter plot and Regression Line).

## How it Works (The Pipeline)
1. **Data Generation:** Synthetic dataset created manually.
2. **Preprocessing:** Separation of Features (Age) and Target (Salary).
3. **Splitting:** 80% for training, 20% for testing.
4. **Modeling:** Fitting a standard Linear Regression model.
5. **Evaluation:** Comparing predicted vs. actual values using Mean Absolute Error (MAE).

## Results & Observations
- The model successfully generated a regression line that approximates the trend: *older age correlates with higher salary in this specific dataset*.
- **Visual Output:** A scatter plot showing real data points (Blue) vs. the model's prediction line (Red).

## Future Improvements
- Test with a larger, real-world dataset.
- Implement other metrics like R² (Coefficient of Determination).
