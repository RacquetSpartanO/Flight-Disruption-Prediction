import streamlit as st
import pandas as pd

hide_sidebar = """
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
"""

st.markdown(hide_sidebar, unsafe_allow_html=True)

st.title("Airline Operations System")

st.write("Air crew")

rdf = pd.read_csv("session_data.csv")
df = pd.DataFrame(rdf)

walkin = st.toggle("Pilot Walk-in Inspection",value=df.iloc[0, df.columns.get_loc("pilot_walkaround_inspection")])
syschk = st.toggle("Aircraft System Checks",value=df.iloc[0, df.columns.get_loc("weather_analysis")])
board = st.slider("Boarding Progress",min_value=0,max_value=100)

df.columns = df.columns.str.strip()
df.iloc[0, df.columns.get_loc("pilot_walkaround_inspection")] = int(walkin)
df.iloc[0, df.columns.get_loc("aircraft_system_checks")] = int(syschk)
df.iloc[0, df.columns.get_loc("boarding_progress")] = int(board)

df.to_csv("session_data.csv", index=False)

if st.button("continue"):
    st.switch_page("main_page.py")