import streamlit as st
import pandas as pd
from exceptions.vehicle_type_not_found_exception import VehicleTypeNotFoundException
from constants import RATES
from service.fare_service import calculate_fare
from database import SessionLocal
from repository.fare_repository import FareRepository

# =============================
# Page Config
# =============================
st.set_page_config(page_title="CityCab Dashboard", page_icon="🚕")

# =============================
# Sidebar Navigation
# =============================
page = st.sidebar.radio(
    "📌 Navigation",
    ["Fare Calculator", "Transactions"]
)

# =============================
# Fare Calculator Page
# =============================
if page == "Fare Calculator":
    st.title("🚕 CityCab Fare Calculator")

    km = st.number_input("Enter Distance (km)", min_value=0.0, step=0.5)

    vehicle_type = st.selectbox(
        "Select Vehicle Type",
        ["ECONOMY", "PREMIUM", "SUV"]
    )

    hour = st.slider("Select Hour (0-23)", 0, 23, 12)

    if st.button("Calculate Fare"):
        try:
            fare, surge = calculate_fare(km, vehicle_type, hour)

            st.success("✅ Fare Calculated Successfully")
            st.subheader("🧾 Ride Estimate")

            st.write(f"**Distance:** {km} km")
            st.write(f"**Vehicle Type:** {vehicle_type}")
            st.write(f"**Rate per km:** ₹{RATES[vehicle_type]}")
            st.write(f"**Travel Hour:** {hour}:00")

            if surge > 1:
                st.warning(f"⚡ Surge Applied: {surge}x (Peak Hours)")
            else:
                st.info("No Surge Applied")

            st.markdown(f"## 💰 Total Fare: ₹{fare:.2f}")

        except VehicleTypeNotFoundException as e:
            st.error(f"❌ {e}")

        except ValueError as e:
            st.error(f"❌ {e}")


# =============================
# Transactions Page
# =============================
elif page == "Transactions":
    st.title("📊 Transactions")

    db = SessionLocal()
    records = FareRepository.get_all(db)
    db.close()

    if records:
        data = [
            {
                "Vehicle": r.vehicle_type,
                "Distance (km)": r.distance_km,
                "Rate/km": r.rate_per_km,
                "Hour": r.travel_hour,
                "Surge": r.surge_multiplier,
                "Type": "Surge" if r.surge_multiplier > 1 else "Normal",
                "Total Fare": r.total_fare
            }
            for r in records
        ]

        df = pd.DataFrame(data)

        # Summary metrics
        st.subheader("📈 Summary")
        col1, col2 = st.columns(2)
        col1.metric("⚡ Surge Rides", df[df["Type"] == "Surge"].shape[0])
        col2.metric("🟢 Normal Rides", df[df["Type"] == "Normal"].shape[0])

        # Filter
        filter_type = st.selectbox("Filter by Type", ["All", "Surge", "Normal"])
        if filter_type != "All":
            df = df[df["Type"] == filter_type]

        # Data table
        st.dataframe(df, use_container_width=True)

    else:
        st.info("No transactions found")