# Habitability_Score_Prediction
Created a smart computer program that predicts how livable a home is on a scale of 1 to 100. Using information from nearly 40,000 properties, I cleaned up messy data, found important patterns, and picked out the most useful details about each home. My first attempt was okay, getting it right about 60% of the time. But then I built a more advanced system using artificial intelligence techniques that got it right 82% of the time, with predictions off by only 4.3 points on average. This smart system looks at 6 key features of a home to make its prediction. To make it easy for anyone to use, I put it online with a simple website where you can enter details about a home and instantly get a livability score. This project shows how we can use technology to help people understand the quality of homes, which could be super useful for buyers, sellers, and real estate professionals.

Website Link: https://habitabilityscoreprediction-kjrmnggewha4b7mhk7suuf.streamlit.app/

## Key Steps

Data Preprocessing: Performed thorough data cleaning to ensure quality input for the model.
Exploratory Data Analysis (EDA): Utilized Seaborn and Matplotlib to gain insights into the dataset's characteristics and relationships.
Feature Engineering & Selection: Employed Lasso Regularization and Correlation Analysis to identify the most impactful features.

## Model Development

Baseline Model: Implemented Linear Regression, achieving an R² score of 60.2%.
Advanced Model: Developed a Multi-Layer Perceptron (MLP) neural network, significantly improving performance:

R² Score: 82.4%
Mean Absolute Error (MAE): 4.3



## MLP Architecture

Input Layer: 6 features
Hidden Layers: 2 layers with ReLU activation
Output Layer: Sigmoid activation
Dropout layer included to prevent overfitting

## Deployment

Deployed the model on Streamlit Cloud
Created an interactive user interface using Streamlit
The UI captures user input and returns a habitability score on a scale of 1 to 100

