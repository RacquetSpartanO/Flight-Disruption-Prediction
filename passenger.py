import streamlit as st

hide_sidebar = """
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
"""
try:
    with open("msg.txt", 'r')as data:
        message = data.read()
except:
    message = "No Notifications"

st.markdown(hide_sidebar, unsafe_allow_html=True)

st.title("Passenger Portal")
st.write("passenger details")

col1, col2 = st.columns([2,1])
if "notfy" not in st.session_state:
    st.session_state.notfy = False

def inc():
    st.session_state.notfy = True

def dec():
    st.session_state.notfy = False

with col1:
    st.button("Flight details")
    st.button("Notifications", on_click=inc)
    if st.button("Home"):
        st.switch_page("main_page.py")
if st.session_state.notfy == True:
    with col2:
        st.markdown(f"<span style='size:20;font-weight:bold'>{"Notifications"}</span>",unsafe_allow_html=True)
        st.markdown(f"<span style='color:red;font-weight:bold'>{message}</span>",unsafe_allow_html=True)
        if st.button("Wait"):
            st.write("Thank you for confirmation")
        if st.button("Refund"):
            st.write("Refund process initiated, money will be credited to your bank account in 2-3 working days")
        if st.button("Book next available flight"):
            with open("flight.txt",'r')as fl:
                if fl == 'True':
                    st.write("Opting dual ticket")
                else:
                    st.markdown(f"<span style='color:red'>No flights available</span>",unsafe_allow_html=True)

        st.button("Back", on_click=dec)
