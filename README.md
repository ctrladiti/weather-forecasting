# 🌦️ Weather Forecasting Dashboard

A real-time, interactive dashboard to visualize temperature, wind speed, humidity, and other forecast data for any city worldwide — powered by Open-Meteo API and built using Streamlit and Python.

---

## 📌 Overview

This project allows users to:

* Search any city and get **daily weather forecasts** for the next 1–7 days
* View **interactive plots** of average temperature, humidity, windspeed, and pressure
* Utilize free and open **weather API** data
* Explore a clean, dashboard-style UI built with **Streamlit**

---

## 🚀 Features

- Input any global city (via geolocation lookup)
- Select number of forecast days (1 to 7)
- Daily aggregated temperature (avg, min, max)
- Real-time humidity, windspeed, and pressure plots
- Responsive dashboard layout with KPI-style info boxes
- Streamlit-powered frontend — deployable instantly

---

## 🖼️ Demo

<img src="assets/demo_dashboard.png" alt="Weather Forecasting Dashboard Demo" width="800"/>

> *Forecast for 5 days in New York City with temperature, humidity, and windspeed trends.*

---

## 🛠️ Tech Stack

| Layer       | Tools & Libraries                         |
| ----------- | ----------------------------------------- |
| UI          | [Streamlit](https://streamlit.io)         |
| Plots       | Plotly, Matplotlib                        |
| Data        | [Open-Meteo API](https://open-meteo.com/) |
| Processing  | Pandas, Requests, Geopy                   |
| Environment | Python, VS Code                       |

---

## 📂 Project Structure

```
weather-dashboard/
│
├── app.py                    # Main Streamlit dashboard script
├── requirements.txt    
└── README.md                 # This file
```

---

## 🧪 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/weather-dashboard.git  
cd weather-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📦 API Used – Open-Meteo

* Fully free and open
* Supports hourly and daily forecast data
* No API key required
* Returns temperature, humidity, windspeed, pressure, precipitation, etc.

[Explore the Open-Meteo API](https://open-meteo.com/en/docs)

---

## 🌍 Future Enhancements

* [ ] Add map-based city picker
* [ ] Enable weather condition icons (rainy, sunny, etc.)
* [ ] Integrate alerts for extreme weather
* [ ] Add historical trends + ML-based future prediction
* [ ] Host app on Streamlit Cloud / Hugging Face Spaces

---

## 📌 Learning Outcomes

This project demonstrates:

* **API Integration** – Making RESTful requests and parsing JSON
* **Data Processing** – Aggregating hourly data into readable daily summaries
* **Dashboard Design** – Clean, intuitive Streamlit layout
* **Problem Solving** – Converting a real-world scenario into an interactive tool
* **Project Deployment Readiness** – Modular, readable code ready for hosting

---

## Acknowledgements

* [Open-Meteo](https://open-meteo.com/) for weather data
* [Geopy](https://pypi.org/project/geopy/) for city-to-coordinate conversion
* [Streamlit](https://streamlit.io/) for making dashboards fast and fun

---

## 💼 Author

**Aditi Agrawal**
[GitHub](https://github.com/Aditi-1304) | [LinkedIn](https://www.linkedin.com) | [Portfolio](https://your-portfolio-link)

