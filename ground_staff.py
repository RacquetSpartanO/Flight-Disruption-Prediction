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

st.write("Ground Staff")

rdf = pd.read_csv("session_data.csv")
df = pd.DataFrame(rdf)

cbn_clg = st.toggle("Cabin Cleaning",value=df.iloc[0, df.columns.get_loc("cabin_cleaning")])
cate = st.toggle("Catering Load",value=df.iloc[0, df.columns.get_loc("catering_loading")])
carg = st.toggle("Cargo Loading",value=df.iloc[0, df.columns.get_loc("cargo_loading")])
fuel_l = st.toggle("Fuel Loading",value=df.iloc[0, df.columns.get_loc("fuel_complete")])
safe_cr = st.toggle("Safety Checks",value=df.iloc[0, df.columns.get_loc("safety_crew_tasks")])

df.columns = df.columns.str.strip()
df.iloc[0, df.columns.get_loc("cabin_cleaning")] = int(cbn_clg)
df.iloc[0, df.columns.get_loc("catering_loading")] = int(cate)
df.iloc[0, df.columns.get_loc("cargo_loading")] = int(carg)
df.iloc[0, df.columns.get_loc("fuel_complete")] = int(fuel_l)
df.iloc[0, df.columns.get_loc("safety_crew_tasks")] = int(safe_cr)

df.to_csv("session_data.csv", index=False)

if st.button("continue"):
    st.switch_page("main_page.py")