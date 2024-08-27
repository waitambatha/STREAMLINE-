# Streamline App

## Overview

This Streamlit application visualizes data from a PostgreSQL database. The database connection details are securely managed through environment variables stored in the `.env` file.

## Prerequisites

- Python 3.x
- PostgreSQL database
- Required Python packages (listed in `requirements.txt`)

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:waitambatha/STREAMLINE-.git
cd STREAMLINE-
2. Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure Environment Variables
Rename .env.example to .env:

bash
Copy code
cp .env.example .env
Edit .env with your PostgreSQL connection details:

Open .env in a text editor and set the following values:

plaintext
Copy code
# Database connection settings
DB_HOST=localhost
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password

# Optional: Add other configuration settings as needed
SECRET_KEY=your_secret_key
DEBUG=True
DB_HOST: The hostname of your PostgreSQL server (e.g., localhost).
DB_NAME: The name of your PostgreSQL database.
DB_USER: Your PostgreSQL username.
DB_PASSWORD: The password for your PostgreSQL user.
SECRET_KEY: (Optional) A secret key for cryptographic operations.
DEBUG: Set to True for development mode or False for production.
5. Run the Application
bash
Copy code
streamlit run app.py
Usage
Once the application is running, open your browser and navigate to the local URL provided by Streamlit to view and interact with your data visualizations.

.env File
The .env file is crucial for configuring the database connection. Ensure that the file is properly set up with your own credentials and is placed in the root directory of your project.

Example .env File
plaintext
Copy code
# Database connection settings
DB_HOST=localhost
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password

# Optional: Add other configuration settings as needed
SECRET_KEY=your_secret_key
DEBUG=True
