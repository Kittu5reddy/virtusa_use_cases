
from service.fare_service import calculate_fare
from exceptions.vehicle_type_not_found_exception import VehicleTypeNotFoundException
from constants import RATES
#==========================
# C O M M A N D L I N E
#==========================
def command_line_main():
    """
    Entry point for the Fare Calculator application.

    Handles:
        - User input
        - Calling fare calculation logic
        - Displaying formatted receipt
        - Error handling for invalid inputs

    This function interacts with the user via console I/O.
    """
    print("Welcome to CityCab Fare Calculator")
    print()

    try:
        km = float(input("Enter distance (in km): "))
        vehicle_type = input("Enter vehicle type (Economy/Premium/SUV): ").upper()
        hour = int(input("Enter hour of travel (0-23): "))

        fare, surge = calculate_fare(km, vehicle_type, hour)

        print("\n Ride Estimate Receipt")
        print("----------------------------")
        print(f"Distance       : {km} km")
        print(f"Vehicle Type   : {vehicle_type}")
        print(f"Rate per km    : ₹{RATES[vehicle_type]}")
        print(f"Travel Hour    : {hour}:00")
        if surge > 1:
            print(f"Surge Applied  : {surge}x (Peak Hours)")
        else:
            print("Surge Applied  : No")
        print(f"Total Fare     : ₹{round(fare, 2)}")
        print("----------------------------")
    except VehicleTypeNotFoundException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Invalid input! Please enter correct values.")

if __name__=="__main__":
    # init_db.py
    from database import engine
    from database.model import Base

    Base.metadata.create_all(bind=engine)
    command_line_main()
