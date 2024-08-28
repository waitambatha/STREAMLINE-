import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
def load_data():
    try:
        data = pd.read_csv('housing.csv')
        return data
    except FileNotFoundError:
        st.error("File 'housing.csv' not found. Please upload the file.")
        return pd.DataFrame()

data = load_data()

if not data.empty:
    st.title("House Price Prediction")

    # Display the dataset
    st.subheader("Dataset")
    st.write(data.head())

    # Split the dataset into features and target
    X = data[['Rooms', 'Size', 'Age']]
    y = data['Price']

    # Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train a Linear Regression model
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.subheader("Model Performance")
    st.write(f"Mean Squared Error: {mse:.2f}")
    st.write(f"R-squared: {r2:.2f}")

    # Get user input
    st.subheader("Enter the House Features")
    rooms = st.number_input("Number of Rooms", min_value=1, max_value=10, value=3)
    size = st.number_input("Size of the House (in square feet)", min_value=500, max_value=5000, value=1500)
    age = st.number_input("Age of the House (in years)", min_value=0, max_value=100, value=10)

    # Predict the house price
    input_data = np.array([[rooms, size, age]])
    input_data_scaled = scaler.transform(input_data)
    predicted_price = model.predict(input_data_scaled)[0]

    # Display the prediction
    st.subheader("Predicted House Price")
    st.write(f"The predicted price of the house is ${predicted_price:.2f}")

    # Graphical representation of the data at the bottom
    st.subheader("Data Visualization")

    # Scatter plot: Price vs Size
    st.write("Scatter plot: Price vs Size")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Size', y='Price', hue='Rooms', palette='viridis')
    plt.title("House Price vs Size (Colored by Number of Rooms)")
    plt.xlabel("Size (square feet)")
    plt.ylabel("Price")
    st.pyplot(plt)
