import streamlit as st

def calculate_emissions(activity, activity_amount):
    # ... (Your emission factors dictionary)

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
        threshold = 421  # Set your threshold here
        if emissions > threshold:
            st.markdown(
                """
                <span style="color: red; font-weight: bold">Danger: High Emissions!</span>
                """,
                unsafe_allow_html=True,
            )
            st.write(
                f"Estimated CO2 Emissions: {emissions:.2f} kg (Exceeds threshold)"
            )

            if st.button("Send Alert Email"):
                # Add your email sending code using the send_alert_email function you've defined earlier
        else:
            st.write(f"Estimated CO2 Emissions: {emissions:.2f} kg (Safe)")
    else:
        st.write("Unknown activity type. Please contact the developer.")
