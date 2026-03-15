import streamlit as st
import pandas as pd
import qrcode as qr
from PIL import Image

hide_sidebar = """
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
"""

st.markdown(hide_sidebar, unsafe_allow_html=True)

st.title("Airline System Login")

col1, col2 = st.columns([2,1])

def Exit():
    rdf = pd.read_csv("session_data.csv")
    df = pd.DataFrame(rdf)
    df.iloc[0, df.columns.get_loc("time_to_departure")] = 0
    df.iloc[0, df.columns.get_loc("fuel_calculation")] = 0
    df.iloc[0, df.columns.get_loc("weather_analysis")] = 0
    df.iloc[0, df.columns.get_loc("cabin_cleaning")] = 0
    df.iloc[0, df.columns.get_loc("safety_crew_tasks")] = 0
    df.iloc[0, df.columns.get_loc("pilot_walkaround_inspection")] = 0
    df.iloc[0, df.columns.get_loc("aircraft_system_checks")] = 0
    df.iloc[0, df.columns.get_loc("fuel_complete")] = 0
    df.iloc[0, df.columns.get_loc("catering_loading")] = 0
    df.iloc[0, df.columns.get_loc("cargo_loading")] = 0
    df.iloc[0, df.columns.get_loc("boarding_progress")] = 0
    df.to_csv("session_data.csv", index=False)
    st.stop()

with col1:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "dispatcher" and password == "1234":
            st.session_state["logged_in"] = True
            st.session_state["role"] = "dispatcher"
            st.switch_page("pages/flight_dispatcher.py")

        elif username == "admin" and password == "admin123":
            st.session_state["logged_in"] = True
            st.session_state["role"] = "admin"
            st.switch_page("pages/admin.py")

        elif username == "groundst" and password == "ground123":
            st.session_state["logged_in"] = True
            st.session_state["role"] = "ground staff"
            st.switch_page("pages/ground_staff.py")

        elif username == "aircrew" and password == "air123":
            st.session_state["logged_in"] = True
            st.session_state["role"] = "air crew"
            st.switch_page("pages/aircrew.py")

        elif username == "passenger" and password == "pass123":
            st.session_state["logged_in"] = True
            st.session_state["role"] = "passenger"
            st.switch_page("pages/passenger.py")

        else:
            st.error("Invalid credentials")

    st.button("Exit",on_click=Exit)

with col2:
    url = "http://10.197.111.8:8501"

    img = qr.make(url)
    img = img.get_image()

    st.image(img, caption=f"Scan to open mobile control panel (or) \nenter url: {url}")