import streamlit as st

st.title("Airline Delay Monitor")

fuel = st.checkbox("Fueling complete")
maintenance = st.checkbox("Maintenance complete")
boarding = st.checkbox("Boarding started")

progress = (fuel + maintenance + boarding) / 3

st.progress(progress)

if progress < 0.7:
    st.warning("High delay risk")
else:
    st.success("Flight likely on time")