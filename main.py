import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Smart Campus Waste Management System", layout="wide")
st.markdown("""
<style>
.stApp{
    background-color:#e8f5e9;
}
h1{
    color:#1b5e20;
}
</style>
""", unsafe_allow_html=True)

st.title("🗑 Smart Campus Waste Management System")
st.caption("SKSJIT Engineering College | Smart Campus Project")
st.write("📅 Date:", datetime.now().strftime("%d-%m-%Y"))

st.header("Smart Dustbin Monitoring Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📍 Location", "Library")

with col2:
    st.metric("🗑 Dustbin ID", "DB-001")

with col3:
    st.metric("🕒 Last Cleaned", "10:30 AM")

st.write("### Select Dustbin")
dustbin = st.selectbox(
    "",
    ["Dustbin 1 - Library", "Dustbin 2 - Canteen", "Dustbin 3 - Main Gate"]
)

level = st.slider(
    "Dustbin Fill Level (%)",
    min_value=0,
    max_value=100,
    value=20,
    key="level"
)

st.progress(level)
st.write(f"Current Fill Level: {level}%")

st.metric("🔋 Battery Status", "92%")
st.metric("📡 Sensor Status", "Active")

st.subheader("🧹 Cleaning Status")

if level >= 90:
    st.error("Cleaning Required Immediately!")
else:
    st.success("Dustbin is functioning normally.")

if level < 70:
    st.success("✅ Campus is clean. No action required.")
elif level < 90:
    st.warning("⚠ Cleaning staff should prepare.")
else:
    st.error("🚨 Immediate cleaning required to prevent overflow.")

st.write("### Sensor Status")

if level < 70:
    st.success("🟢 Dustbin Status : Normal")
    st.write("💡 LED : Green")
    st.write("🔔 Buzzer : OFF")
    st.write("📩 Staff Alert : Not Required")

elif level < 90:
    st.warning("🟡 Dustbin Almost Full")
    st.write("💡 LED : Yellow")
    st.write("🔔 Buzzer : OFF")
    st.write("📩 Staff Alert : Cleaning Staff Ready")

else:
    st.error("🔴 Dustbin FULL!")
    st.write("💡 LED : Red")
    st.write("🔔 Buzzer : ON")
    st.write("📩 Alert Sent to Cleaning Staff")

    if st.button("📨 Send Alert Again"):
        st.success("✅ Alert Successfully Sent!")

        st.write("### 📊 Waste Collection Statistics")

data = pd.DataFrame({
    "Location": ["Library", "Canteen", "Main Gate"],
    "Fill Level": [20, 65, 90]
})

st.bar_chart(data.set_index("Location"))

st.write("### 🧹 Maintenance")

if st.button("🗑 Clean Dustbin"):
    st.session_state["level"] = 0
    st.rerun()