# PostgreSQL Data Visualization with Streamlit

This is a Streamlit application designed to connect to a PostgreSQL database and visualize data. The app allows users to enter SQL queries to retrieve data from a PostgreSQL database and visualize it using interactive charts.

## Features

- **Fetch Data:** Enter SQL queries to fetch data from a PostgreSQL database.
- **Display Data:** View the retrieved data in a tabular format.
- **Visualize Data:** Generate visualizations using Plotly (e.g., bar charts) based on the retrieved data.

## Prerequisites

Before running the app, ensure you have the following installed:

- **Python 3.6+**: Streamlit and other dependencies require Python.
- **Streamlit**: For creating the web application.
- **Psycopg2**: PostgreSQL adapter for Python.
- **Pandas**: Data manipulation and analysis library.
- **Plotly**: Library for interactive data visualization.

You can install these dependencies using pip:

```bash
pip install streamlit psycopg2 pandas plotly
Configuration
Update the db_params dictionary in app.py with your PostgreSQL database credentials:

python
Copy code
db_params = {
    'host': 'localhost',
    'database': 'stream',
    'user': 'postgres',
    'password': 'Mbatha45'
}
host: The hostname of your PostgreSQL server (e.g., localhost).
database: The name of the PostgreSQL database (e.g., stream).
user: The PostgreSQL username (e.g., postgres).
password: The PostgreSQL password.
Usage
Save the Streamlit application code to a file named app.py.

Open a terminal and navigate to the directory where app.py is located.

Run the Streamlit app using:

bash
Copy code
streamlit run app.py
The application will open in your default web browser. Enter your SQL query into the provided text area and click the "Fetch Data" button to retrieve and visualize the data.

Example Queries
You can use SQL queries such as:

SELECT * FROM your_table_name LIMIT 100; to retrieve data from a specific table.
Customize the SQL query based on the schema and data in your PostgreSQL database.
Troubleshooting
Error Fetching Data: Ensure your PostgreSQL server is running and the connection parameters are correct.
Empty Data or Missing Columns: Verify that your SQL query returns the expected columns and data.
