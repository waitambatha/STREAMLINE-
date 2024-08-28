# House Price Prediction App

This is a Streamlit application that predicts house prices based on user inputs using a Linear Regression model. The app allows users to input features such as the number of rooms, size, and age of the house, and provides a predicted price based on the trained model.

## Features

- **House Price Prediction**: Enter the number of rooms, size (in square feet), and age (in years) of the house to get the predicted price.
- **Data Visualization**: Scatter plot showing the relationship between house size and price, colored by the number of rooms.
- **Model Performance Metrics**: Displays Mean Squared Error and R-squared value for the model to evaluate its performance.

## Requirements

To run this application, you need to have the following Python libraries installed:

- `streamlit`
- `pandas`
- `scikit-learn`
- `numpy`
- `seaborn`
- `matplotlib`

You can install these libraries using the `requirements.txt` file.

## Installation

1. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Prepare the dataset:**

   Ensure you have the `housing.csv` file in the root directory of the project. This file should contain the data with columns: `Rooms`, `Size`, `Age`, and `Price`.

3. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

4. **Access the app:**

   Open a web browser and go to `http://localhost:8501` to view and interact with the app.

## Usage

- On the main page, you will see the dataset displayed.
- Enter the house features in the input fields on the sidebar.
- Click on "Submit" to get the predicted house price.
- The scatter plot visualizes the relationship between house size and price.

## Model Details

- **Algorithm**: Linear Regression
- **Features Used**: Rooms, Size, Age
- **Metrics**:
  - Mean Squared Error
  - R-squared

