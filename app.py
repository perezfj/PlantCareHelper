import streamlit as st
import pandas as pd

st.set_page_config(page_title="🌱 Plant Care Helper", layout="wide")

# Title and introduction
st.title("🌿 Plant Care Helper")
st.subheader("Your basic guide to keeping houseplants healthy.")

# Sidebar with plant selection
st.sidebar.title("Options")
plant = st.sidebar.selectbox("Select a plant", ["Monstera", "Cactus", "Aloe Vera", "Orchid"])

# Simulated plant care data
plant_data = {
    "Monstera": {"Watering": "Twice a week", "Light": "Indirect light", "Temperature": "64–80°F (18–27°C)"},
    "Cactus": {"Watering": "Every 10 days", "Light": "Direct sunlight", "Temperature": "70–85°F (21–29°C)"},
    "Aloe Vera": {"Watering": "Every 2 weeks", "Light": "Bright light", "Temperature": "66–77°F (19–25°C)"},
    "Orchid": {"Watering": "Once a week", "Light": "Indirect light", "Temperature": "60–75°F (16–24°C)"},
}

# Display care instructions in a table
st.markdown(f"### Care Instructions for {plant}")
df = pd.DataFrame([plant_data[plant]])
st.dataframe(df)

# Divider
st.markdown("---")

# Interactive widgets section
st.markdown("### Customize Your Experience")

name = st.text_input("Enter your name:")
fav_color = st.color_picker("Pick your favorite color:", "#6fdc8c")
watering_pref = st.slider("How many days between waterings do you prefer?", 1, 30, 7)

# Checkbox for reminders
if st.checkbox("Would you like to receive watering reminders?"):
    st.success("Reminders activated!")

# Simulate diagnosis button
if st.button("Simulate Diagnosis"):
    st.info("This feature will be available soon 😊")

# Divider
st.markdown("---")

# Bar chart for watering frequency
st.markdown("### Watering Frequency by Plant (in days)")
watering_days = {
    "Monstera": 3,
    "Cactus": 10,
    "Aloe Vera": 14,
    "Orchid": 7
}
chart_df = pd.DataFrame({
    "Plant": list(watering_days.keys()),
    "Watering Interval (days)": list(watering_days.values())
})
st.bar_chart(chart_df.set_index("Plant"))

# Divider
st.markdown("---")

# Map of plant-friendly locations (simulated)
st.markdown("### Common Growth Areas (Simulated)")
map_data = pd.DataFrame({
    'lat': [25.7617, 34.0522, 40.7128],  # Miami, LA, NYC
    'lon': [-80.1918, -118.2437, -74.0060]
})
st.map(map_data)

