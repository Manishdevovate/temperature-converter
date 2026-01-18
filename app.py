import streamlit as st
import time

# 1. Setup the page configuration (Tab title and icon)
st.set_page_config(page_title="Time Traveler Converter", page_icon="⏰")

# 2. Add a Sidebar for input
st.sidebar.header("⚙️ Settings")
mode = st.sidebar.radio("Select Conversion Mode:", ["Celsius ➡ Fahrenheit", "Fahrenheit ➡ Celsius"])

# 3. Main Page Design
st.title("🌡️ Temperature Converter")
st.markdown("Convert temperatures accurately for your time travel logs.")
st.divider() # Adds a visual line

# 4. Input Number
temp = st.number_input("Enter Temperature:", value=0.0, step=1.0)

# 5. The Trigger
if st.button("Convert Now", type="primary"):
    
    # Add a fake "processing" bar for visual effect
    with st.spinner('Calculating physics...'):
        time.sleep(0.5) # Pauses for half a second
    
    # Logic
    if mode == "Celsius ➡ Fahrenheit":
        res = f"{temp * 1.8 + 32:.2f}°F"
        st.success(f"📍 {temp}°C = {res}")
    else:
        res = f"{(temp - 32) / 1.8:.2f}°C"
        st.success(f"📍 {temp}°F = {res}")
        
    # Celebration animation
    st.balloons()

# 6. Footer
st.markdown("---")
st.caption("🚀 Built with Python & Streamlit")
