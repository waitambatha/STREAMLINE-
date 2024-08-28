import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection parameters from .env
db_params = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# Create a function to fetch data from the database
def fetch_data(query):
    try:
        conn = psycopg2.connect(**db_params)
        data = pd.read_sql_query(query, conn)
        conn.close()
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error

# Streamlit app
st.title('PostgreSQL Data Visualization')

# Input query from the user
query = st.text_area('Enter SQL query to fetch data:', 'SELECT * FROM car_data LIMIT 100;')

if st.button('Fetch Data'):
    if query:
        data = fetch_data(query)
        if not data.empty:
            st.write('Data retrieved from database:')
            st.dataframe(data)

            # Example: Plotting a bar chart using Plotly
            if 'car_model' in data.columns and 'mpg' in data.columns:
                fig = px.bar(data, x='car_model', y='mpg', title='Car Model vs MPG')
                st.plotly_chart(fig)
            else:
                st.warning('Columns "car_model" and "mpg" are not present in the data.')
        else:
            st.warning('No data available or query returned an empty result.')
    else:
        st.error('Please enter a valid SQL query.')
