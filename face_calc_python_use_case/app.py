import streamlit as st

# Import your existing logic
try:
    from service import calculate_fare, RATES, VehicleTypeNotFoundException
except ModuleNotFoundError:
    from service import calculate_fare, RATES, VehicleTypeNotFoundException

# Page config
st.set_page_config(page_title="CityCab Fare Calculator", page_icon="🚕")

st.title("🚕 CityCab Fare Calculator")
st.write("Calculate your ride estimate instantly!")






# =============================
# User Inputs
# =============================
km = st.number_input("Enter Distance (km)", min_value=0.0, step=0.5)









vehicle_type = st.selectbox(
    "Select Vehicle Type",
    options=["ECONOMY", "PREMIUM", "SUV"]
)









hour = st.slider("Select Hour of Travel (0-23)", 0, 23, 12)






# =============================
# Calculate Button
# =============================
if st.button("Calculate Fare"):
    try:
        fare, surge = calculate_fare(km, vehicle_type, hour)
        st.success("✅ Fare Calculated Successfully!")
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