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

st.write("Flight Dispatcher")

rdf = pd.read_csv("session_data.csv")
df = pd.DataFrame(rdf)

fuel_calc = st.toggle("Fuel Calculations",value=df.iloc[0, df.columns.get_loc("fuel_calculation")])
wthr_alys = st.toggle("Weather Analysis",value=df.iloc[0, df.columns.get_loc("weather_analysis")])
deptime = st.text_input("Time left for Departue (in minutes)",value=df.iloc[0, df.columns.get_loc("time_to_departure")])

df.columns = df.columns.str.strip()
df.iloc[0, df.columns.get_loc("fuel_calculation")] = int(fuel_calc)
df.iloc[0, df.columns.get_loc("weather_analysis")] = int(wthr_alys)
df.iloc[0, df.columns.get_loc("time_to_departure")] = int(deptime)

df.to_csv("session_data.csv", index=False)

if st.button("continue"):
    st.switch_page("main_page.py")