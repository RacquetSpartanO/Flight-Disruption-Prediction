import streamlit as st
import pandas as pd
import joblib

hide_sidebar = """
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
"""

Pipe = joblib.load(r"D:\DP project\IV SEM\Thinkathon\flightdelay_pred_model.pkl")

st.markdown(hide_sidebar, unsafe_allow_html=True)

st.title("Airline Operations System")

st.write("Admin Page")

col1, col2 = st.columns([2,1])

daf = pd.read_csv("session_data.csv")
df = pd.DataFrame(daf)
df.columns = df.columns.str.strip()

pred = list(Pipe.predict_proba(df))
delay_probability = pred[0][1] * 100

fuel_c = df.iloc[0, df.columns.get_loc("fuel_calculation")]
wthr_a = df.iloc[0, df.columns.get_loc("weather_analysis")]
cab = df.iloc[0, df.columns.get_loc("cabin_cleaning")]
cat = df.iloc[0, df.columns.get_loc("catering_loading")]
cargo = df.iloc[0, df.columns.get_loc("cargo_loading")]
fuel_load = df.iloc[0, df.columns.get_loc("fuel_complete")]
safech = df.iloc[0, df.columns.get_loc("safety_crew_tasks")]
pilotwalk = df.iloc[0, df.columns.get_loc("pilot_walkaround_inspection")]
systemchk = df.iloc[0, df.columns.get_loc("aircraft_system_checks")]
boarding = df.iloc[0, df.columns.get_loc("boarding_progress")]
time = df.iloc[0, df.columns.get_loc("time_to_departure")]

if boarding <= 50 and time <= 15:
    delay_probability += 10

if fuel_load == 0 and time <= 8:
    delay_probability += 10

if cargo == 0 and time <= 20:
    delay_probability += 10

if delay_probability >= 100:
    delay_probability = 100

#fuel calc
if fuel_c == 1:
    fuel_c = "Completed"
else:
    fuel_c = "Not Completed"

#weather analysis
if wthr_a == 1:
    wthr_a = "Completed"
else:
    wthr_a = "Not Completed"

#cabin clean
if cab == 1:
    cab = "Completed"
else:
    cab = "Not Completed"

#catering
if cat == 1:
    cat = "Completed"
else:
    cat = "Not Completed"

#cargo
if cargo == 1:
    cargo = "Completed"
else:
    cargo = "Not Completed"

#fuel loading
if fuel_load == 1:
    fuel_load = "Completed"
else:
    fuel_load = "Not Completed"

#safety checks
if safech == 1:
    safech = "Completed"
else:
    safech = "Not Completed"

#pilot walkin check
if pilotwalk == 1:
    pilotwalk = "Completed"
else:
    pilotwalk = "Not Completed"

#aircraft system check
if systemchk == 1:
    systemchk = "Completed"
else:
    systemchk = "Not Completed"


with col1:
    st.info("Crew members update their status here. Admin monitors progress.")

    color = "green" if time >= 60 else "red"
    st.markdown(f"Time Left for Departure: <span style='color:{color};font-weight:bold'>{time}</span>",unsafe_allow_html=True)
    color = "green" if fuel_c.lower() == "completed" else "red"
    st.markdown(f"Fuel Calculation Status: <span style='color:{color};font-weight:bold'>{fuel_c}</span>",unsafe_allow_html=True)
    color = "green" if wthr_a.lower() == "completed" else "red"
    st.markdown(f"Weather Analysis Status: <span style='color:{color};font-weight:bold'>{wthr_a}</span>",unsafe_allow_html=True)
    color = "green" if safech.lower() == "completed" else "red"
    st.markdown(f"Safety Checking Status: <span style='color:{color};font-weight:bold'>{safech}</span>",unsafe_allow_html=True)
    color = "green" if cab.lower() == "completed" else "red"
    st.markdown(f"Cabin Cleaning Status: <span style='color:{color};font-weight:bold'>{cab}</span>",unsafe_allow_html=True)
    color = "green" if cat.lower() == "completed" else "red"
    st.markdown(f"Catering Loading Status: <span style='color:{color};font-weight:bold'>{cat}</span>",unsafe_allow_html=True)
    color = "green" if cargo.lower() == "completed" else "red"
    st.markdown(f"Cargo Loading Status: <span style='color:{color};font-weight:bold'>{cargo}</span>",unsafe_allow_html=True)
    color = "green" if fuel_load.lower() == "completed" else "red"
    st.markdown(f"Fuel Loading Status: <span style='color:{color};font-weight:bold'>{fuel_load}</span>",unsafe_allow_html=True)
    color = "green" if pilotwalk.lower() == "completed" else "red"
    st.markdown(f"Pilot Walk-in Checking Status: <span style='color:{color};font-weight:bold'>{pilotwalk}</span>",unsafe_allow_html=True)
    color = "green" if systemchk.lower() == "completed" else "red"
    st.markdown(f"Aircraft System Checking Status: <span style='color:{color};font-weight:bold'>{systemchk}</span>",unsafe_allow_html=True)
    color = "green" if boarding >= 75 else "red"
    st.markdown(f"Boarding Status: <span style='color:{color};font-weight:bold'>{boarding}%</span>",unsafe_allow_html=True)
    color = "green" if delay_probability <= 15 else "red"
    st.markdown(f"Delay Prediction: <span style='color:{color};font-weight:bold'>{delay_probability:.2f}%</span>",unsafe_allow_html=True)

    if st.button("Main Page"):
        st.switch_page("main_page.py")

def notify_passenger(x):
    with open("msg.txt", 'w') as msg:
        msg.write(f"The possibility of your flight being {x} is high!")

with col2:
    if delay_probability >= 65:
            st.markdown(f"<span style='color:{color};font-weight:bold'>The Probability of the flight being delayed is high</span>",unsafe_allow_html=True)
            st.button('Notify Passengers', on_click=notify_passenger("DELAYED"))
            if st.button("Arrange Backup flight"):
                with open ("flight.txt", 'w') as fli:
                    fli.write('True')
                    
            else:
                with open ("flight.txt", 'w') as fli:
                    fli.write('False')
    if delay_probability >= 100:
            st.markdown(f"<span style='color:{color};font-weight:bold'>The Probability of the flight being cancelled is high</span>",unsafe_allow_html=True)
            st.button('Notify Passengers', on_click=notify_passenger("CANCELLED"))