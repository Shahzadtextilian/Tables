import streamlit as st
import pandas as pd

# Title of the app
st.title("Multiplication Table Generator")

# Input for the number and the range of the table
number = st.number_input("Enter a number to generate the multiplication table", min_value=1, value=5)
table_range = st.number_input("Enter the range (e.g., 10 for table up to 10)", min_value=1, value=10)

# Generate the multiplication table
table = {f"{number} x {i}": number * i for i in range(1, table_range + 1)}

# Display the table as a DataFrame
df = pd.DataFrame(list(table.items()), columns=["Expression", "Result"])
st.write(f"Multiplication Table of {number} up to {table_range}:")
st.dataframe(df)
