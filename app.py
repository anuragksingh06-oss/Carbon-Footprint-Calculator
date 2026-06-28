import streamlit as st

# Emission factors dictionary for all countries in the select box
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1,
    },
    "China": {
        "Transportation": 0.2,
        "Electricity": 0.6,
        "Diet": 1.4,
        "Waste": 0.2,
    },
    "Japan": {
        "Transportation": 0.15,
        "Electricity": 0.5,
        "Diet": 1.1,
        "Waste": 0.05,
    },
    "Canada": {
        "Transportation": 0.18,
        "Electricity": 0.7,
        "Diet": 1.3,
        "Waste": 0.12,
    },
    "New Zealand": {
        "Transportation": 0.12,
        "Electricity": 0.4,
        "Diet": 1.0,
        "Waste": 0.08,
    }
}

# Country-specific CO2 warning messages
WARNING_MESSAGES = {
    "India": {
        "In 2023, CO2 emissions per capita for India were 2.07 tons of CO2 per capita. "
        "Between 1972 and 2023, CO2 emissions per capita in India grew substantially, "
        "rising from 0.39 to 2.07 tons at an increasing annual rate."
    },
    "China": {
        "In 2023, China had one of the highest CO2 emissions per capita globally. Rapid industrial growth "
        "and urbanization have led to substantial increases in CO2 emissions over recent decades."
    },
    "Japan": {
        "Japan’s CO2 emissions per capita were around 8.9 tons in 2023, largely due to energy needs in "
        "transportation and industry, although the country has made progress in renewable energy adoption."
    },
    "Canada": {
        "Canada’s CO2 emissions per capita were approximately 14.2 tons in 2023, among the highest "
        "globally, driven by high energy consumption, transportation, and resource-based industries."
    },
    "New Zealand": {
        "New Zealand’s CO2 emissions per capita were about 6.9 tons in 2023, mainly from agriculture and "
        "energy production, though the country is working towards reducing its footprint."
    },
}

st.set_page_config(page_title="Carbon Footprint Calculator")

st.title("Carbon Footprint Calculator")

st.subheader("🌍 Your Country")
country = st.selectbox("Select", list(EMISSION_FACTORS.keys()))
st.write("Selected Country:", country)  # Debugging statement to confirm country selection

col1, col2 = st.columns(2)

# Input fields for emissions
with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🗑 Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍲 Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

# Annualizing the inputs
distance = distance * 365
electricity = electricity * 12
meals = meals * 365
waste = waste * 52

# Calculating individual emissions
transportation_emission = round(EMISSION_FACTORS[country]['Transportation'] * distance / 1000, 2)
electricity_emission = round(EMISSION_FACTORS[country]['Electricity'] * electricity / 1000, 2)
diet_emission = round(EMISSION_FACTORS[country]['Diet'] * meals / 1000, 2)
waste_emission = round(EMISSION_FACTORS[country]['Waste'] * waste / 1000, 2)

# Calculating total emissions
total_emissions = round(
    transportation_emission + electricity_emission + diet_emission + waste_emission, 2
)

if st.button("Calculate CO2 Emissions"):
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Categories")
        st.info(f"🚗 Transportation: {transportation_emission} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emission} tonnes CO2 per year")
        st.info(f"🍲 Diet: {diet_emission} tonnes CO2 per year")
        st.info(f"🗑 Waste: {waste_emission} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.info(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        
        # Display country-specific warning
        st.warning(WARNING_MESSAGES[country])
