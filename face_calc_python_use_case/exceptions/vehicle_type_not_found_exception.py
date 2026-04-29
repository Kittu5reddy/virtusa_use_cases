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


