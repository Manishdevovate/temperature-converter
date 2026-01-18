import streamlit as st

# Set up the title
st.title("🌡️ Time Traveler's Converter")

# Create the user interface
# This replaces the 'while' loop and 'input' statements
mode = st.radio("Select Mode:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
temp = st.number_input("Enter Temperature:", value=0.0)

# Calculate and display result
if st.button("Convert Now"):
    # This logic is exactly the same as your shortened Python code
    if mode == "Celsius to Fahrenheit":
        res = f"{temp * 1.8 + 32:.2f}°F"
        st.success(f"📍 {temp}°C = {res}")
    else:
        res = f"{(temp - 32) / 1.8:.2f}°C"
        st.success(f"📍 {temp}°F = {res}")