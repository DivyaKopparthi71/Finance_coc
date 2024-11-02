import streamlit as st
import pandas as pd

# Load the data from Google Sheets
sheet_url = 'https://docs.google.com/spreadsheets/d/1lPc5nFXqaTgZuP7EtdoFgNrzKfmvLUsmZi9r4TWlNng/export?format=csv'
data = pd.read_csv(sheet_url)

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
            # Append the new user data to the DataFrame
            new_row = {
                "Name": name,
                "Phone Number": phone_number,
                "Address": address,
                "Mode": mode,
                "Days": days,
                "Months": months,
                "Amount": amount
            }
            data = data.append(new_row, ignore_index=True)
            st.success("New user data added successfully!")
            st.write("Updated Data:", data)

elif user_type == "Old User":
    # Displaying the data from Google Sheets for existing users
    st.write("Existing Users Data")
    st.dataframe(data)

