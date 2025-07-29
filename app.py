import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Weather Dashboard", layout="wide")

# ---------- MAIN TITLE ----------
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🌤 Weather Forecast Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Get 1-7 day forecasts with interactive charts and KPIs</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------- INPUTS ----------
col1, col2 = st.columns([2, 1])
with col1:
    city = st.text_input("Enter City Name", "Delhi")
with col2:
    days_range = st.selectbox("Forecast Range (Days)", [1, 2, 3, 4, 5, 6, 7], index=2)

# ---------- API FUNCTIONS ----------
def get_lat_lon(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&country=IN"
    res = requests.get(url).json()
    if "results" in res:
        return res["results"][0]["latitude"], res["results"][0]["longitude"]
    else:
        return None, None

lat, lon = get_lat_lon(city)

if lat is not None and lon is not None:
    start_date = datetime.today().date()
    end_date = start_date + timedelta(days=days_range - 1)

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,relative_humidity_2m,windspeed_10m,pressure_msl"
        f"&start_date={start_date}&end_date={end_date}&timezone=auto"
    )
    data = requests.get(weather_url).json()

    if "hourly" in data:
        df = pd.DataFrame(data["hourly"])
        df["time"] = pd.to_datetime(df["time"])
        df["date"] = df["time"].dt.date

        st.success(f"Forecast for **{city.title()}** from {start_date} to {end_date}")

        # ---------- KPI METRICS ----------
        avg_temp = df["temperature_2m"].mean().round(2)
        max_wind = df["windspeed_10m"].max().round(1)
        avg_humidity = df["relative_humidity_2m"].mean().round(1)
        min_pressure = df["pressure_msl"].min().round(1)

        st.markdown("### 🔍 Key Weather Stats")
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("Avg Temp (°C)", f"{avg_temp}")
        kpi2.metric("Max Wind (km/h)", f"{max_wind}")
        kpi3.metric("Avg Humidity (%)", f"{avg_humidity}")
        kpi4.metric("Min Pressure (hPa)", f"{min_pressure}")

        # ---------- CHARTS ----------
        st.markdown("### 📊 Forecast Trends")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🌡 Temperature Over Time")
            st.line_chart(df.set_index("time")[["temperature_2m"]])
        with col2:
            st.subheader("💨 Wind Speed Over Time")
            st.line_chart(df.set_index("time")[["windspeed_10m"]])

        col3, col4 = st.columns(2)
        with col3:
            st.subheader("💧 Humidity Over Time")
            st.line_chart(df.set_index("time")[["relative_humidity_2m"]])
        with col4:
            st.subheader("📉 Pressure Over Time")
            st.line_chart(df.set_index("time")[["pressure_msl"]])

        # ---------- DAILY AVERAGES ----------
        daily_avg = df.groupby("date")["temperature_2m"].mean().reset_index()
        daily_avg.columns = ["Date", "Avg Temp (°C)"]

        st.markdown("### 📆 Daily Avg Temperature")
        st.line_chart(daily_avg.set_index("Date"))
        st.dataframe(daily_avg, use_container_width=True)

    else:
        st.warning("Weather data not available.")
else:
    st.error("City not found.")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:0.85rem; color:#aaa;'>Made with ❤️ using Open-Meteo API & Streamlit</p>",
    unsafe_allow_html=True,
)
