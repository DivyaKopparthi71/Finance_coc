import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials for Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("sai-finance.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1lPc5nFXqaTgZuP7EtdoFgNrzKfmvLUsmZi9r4TWlNng/edit#gid=0'
spreadsheet = client.open_by_url(sheet_url)
worksheet = spreadsheet.get_worksheet(0)

# Load data into a DataFrame
data = pd.DataFrame(worksheet.get_all_records())

# Title of the app
st.title("User Information Form")

# User type selection
user_type = st.radio("Select User Type:", ["New User", "Old User"])

if user_type == "New User":
    # Displaying form fields based on sheet columns for a new user
    with st.form("new_user_form"):
        name = st.text_input("Name")
        phone_number = st.text_input("Phone Number")
        address = st.text_input("Address")
        mode = st.selectbox("Mode", ["Days", "Months"])
        days = st.number_input("Days", min_value=0, step=1)
        months = st.number_input("Months", min_value=0, step=1)
        amount = st.number_input("Amount", min_value=0, step=100)

        # Submit button for new user form
        submitted = st.form_submit_button("Submit")
        if submitted:
            # Append the new user data to the Google Sheet
            new_row = [name, phone_number, address, mode, days, months, amount]
            worksheet.append_row(new_row)
            st.success("New user data added successfully!")

elif user_type == "Old User":
    # Displaying the data from Google Sheets for existing users
    st.write("Existing Users Data")
    st.dataframe(data)
