import streamlit as st
import smtplib  # For email functionality
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# ... Additional libraries for video processing
from email.mime.base import MIMEBase
from email import encoders
found=False

def send_alert_email(emissions):

    sender_email = "tempemail719@gmail.com"
    receiver_email = "nageshch9966@gmail.com"
    password = "novtsibhbafgusud"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Danger limit exceeded!"
    message["From"] = sender_email
    message["To"] = receiver_email

    text1 = """\
        hey your vechile producing high emissions!.
        it is estimated that co2 emissions :"""
    text2 = """  kg (exceeds threshold)
  please service your vechile"""
    text = text1 + str(emissions) + text2

    part = MIMEText(text, "plain")
    message.attach(part)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    st.write("email sent")


def calculate_emissions(activity, activity_amount):
    # Sample emission factors - you'll need a more comprehensive source
    emission_factors = {
        "Car (Gasoline)": 0.25,  # kg CO2 per km
        "Electricity": 0.5,  # kg CO2 per kWh
        "Flight": 0.12  # kg CO2 per passenger-km
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

btn2= st.button("Calculate")
if btn2:
    found = False
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

            found=True


        else:

            st.write(f"Estimated CO2 Emissions: {emissions:.2f} kg (Safe)")
        if found:
            btn1=st.button("send alert email")

            if btn1==False:
                st.write("")
                send_alert_email(emissions)
                st.write("email sent")
    else:
        st.write("Unknown activity type. Please contact the developer.")

