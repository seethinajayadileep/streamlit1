import streamlit as st

def calculate_emissions(activity, activity_amount):
    # Sample emission factors - you'll need a more comprehensive source
    emission_factors = {
        "Car (Gasoline)": 0.25,  # kg CO2 per km
        "Electricity": 0.5,     # kg CO2 per kWh
        "Flight": 0.12          # kg CO2 per passenger-km
    }

    if activity in emission_factors:
        emissions = activity_amount * emission_factors[activity]
        return emissions
    else:
        return None

st.title("CO2 Calculator")

activity_type = st.selectbox("Choose Activity Type",
                             ["Car (Gasoline)", "Electricity", "Flight"])

activity_amount = st.number_input("Enter Amount:", min_value=0.0)

if st.button("Calculate"):
    emissions = calculate_emissions(activity_type, activity_amount)
    if emissions:
        st.write(f"Estimated CO2 Emissions: {emissions:.2f} kg")
    else:
        st.write("Unknown activity type. Please contact the developer.")
