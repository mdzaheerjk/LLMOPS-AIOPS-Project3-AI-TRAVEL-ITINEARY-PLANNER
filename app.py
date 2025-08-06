import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itineary Planner")
st.write("Plan your day trip itineary by entering your city and interests")

load_dotenv()

with st.form("planner_form"):
    city = st.text_input("Enter the city name for your trip")
    interests = st.text_input("Enter your interests (comma-seperated )")
    submitted = st.form_submit_button("Generate itineary")

    if submitted:
        if city and interests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itineary = planner.create_itineary()

            st.subheader("📄 Your Itineary")
            st.markdown(itineary)
        else:
            st.warning("Please fill City or Interest to move forward")



