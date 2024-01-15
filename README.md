# Text to SQL Conversion Project
## Overview
Overview
This project demonstrates the use of Google's Gemini Pro API and Streamlit to create a text-to-SQL interface. It involves a Python application that interprets natural language queries and translates them into SQL queries, which are then executed against a SQLite database.


## Technologies Used
- Streamlit
- Google GenerativeAI (Gemini Pro API)
- Python-dotenv

## Setup
1. Obtain the Google Gemini API key from [Google MakerSuite](https://makersuite.google.com/app/apikey).
2. Store the API key in a `.env` file for security.

## Database Setup (`sql.py`)
- The `sql.py` script initializes a SQLite database with dummy data.
- Run `python sql.py` to set up the database.

## Application (`app.py`)
- The `app.py` script uses the Gemini Pro API to convert user questions into SQL queries.
- The generated SQL queries are executed against the SQLite database to fetch the required data.

## Running the Application
- Execute `streamlit run app.py` to start the Streamlit server.
- Interact with the application through the Streamlit user interface.

## Security Note
- API keys and sensitive data are stored securely using environment variables.
"""
