#=============================================
#           R A T E S
#=============================================
RATES = {
    "ECONOMY": 10,
    "PREMIUM": 18,
    "SUV": 25
}


#=============================================
#           E x c e p t i o n
#=============================================
class VehicleTypeNotFoundException(Exception):
    """
    Exception raised when the given vehicle type is not available
    in the rate configuration.

    Attributes:
        message (str): Explanation of the error.
    """
    def __init__(self, message:str):
        super().__init__(message)





#=============================================
#           S e r v i c e L a y e r
#=============================================
def calculate_fare(kilometers:float,vehicle_type:str,hour:int)->tuple[float,float]:
    """
    Calculate the final ride fare based on distance, vehicle type,
    and time of travel (for surge pricing).

    Args:
        kilometers (float): Distance of the ride in kilometers.
        vehicle_type (str): Type of vehicle (ECONOMY, PREMIUM, SUV).
        hour (int): Hour of the day (0 to 23).

    Returns:
        tuple[float, float]:
            - Final fare after applying surge (float)
            - Surge multiplier applied (float)

    Raises:
        ValueError: If hour is not between 0 and 23.
        VehicleTypeNotFoundException: If vehicle type is invalid.
    """
    if not (0 <= hour <= 23):
        raise ValueError("Hour must be between 0 and 23")
    if vehicle_type not in RATES:
        raise VehicleTypeNotFoundException("Vehicle Type Not Found")
    rate=RATES[vehicle_type]
    total_amount=kilometers*rate
    surge=1.0
    if hour>=17 and hour<=20:
        surge=1.5
    return total_amount*surge,surge




#==========================
# C O M M A N D L I N E
#==========================
def main():
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

        print("\n🧾 Ride Estimate Receipt")
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
    main()
