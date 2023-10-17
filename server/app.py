class Vehicle:
    """
    Represents a general vehicle with common properties and methods.

    Attributes:
        make (str): The make of the vehicle.
        model (str): The model of the vehicle.
        fuel_type (str): The type of fuel the vehicle uses.
    """
    def __init__(self, make, model, fuel_type):
        """
        Initializes a new Vehicle instance.

        Args:
            make (str): The make of the vehicle.
            model (str): The model of the vehicle.
            fuel_type (str): The type of fuel the vehicle uses.
        """
        self.make = make
        self.model = model
        self.fuel_type = fuel_type

    def start_engine(self):
        """
        Starts the vehicle's engine.
        """
        print(f"Starting the {self.make} {self.model}'s engine.")

    def stop_engine(self):
        """
        Stops the vehicle's engine.
        """
        print(f"Stopping the {self.make} {self.model}'s engine.")


class Car(Vehicle):
    """
    Represents a specific type of vehicle, a car, with additional attributes and methods.

    Attributes:
        num_doors (int): The number of doors the car has.
    """
    def __init__(self, make, model, fuel_type, num_doors):
        """
        Initializes a new Car instance.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            fuel_type (str): The type of fuel the car uses.
            num_doors (int): The number of doors the car has.
        """
        super().__init__(make, model, fuel_type)
        self.num_doors = num_doors

    def lock_doors(self):
        """
        Locks the car's doors.
        """
        print(f"Locking the doors of the {self.make} {self.model} car.")

    def unlock_doors(self):
        """
        Unlocks the car's doors.
        """
        print(f"Unlocking the doors of the {self.make} {self.model} car.")


class Driver:
    """
    Represents a driver and contains information about their license.

    Attributes:
        name (str): The name of the driver.
        driving_license (License): An instance of the License class containing driving_license information.
    """

    def __init__(self, name, driving_license):
        """
        Initializes a new Driver instance.

        Args:
            name (str): The name of the driver.
            driving_license (License): An instance of the License class containing driving_license information.
        """
        self.name = name
        self.driving_license = driving_license

    def show_driving_license_info(self):
        """
        Displays the driver's name and driving_license information.
        """
        print(f"Driver: {self.name}")
        self.driving_license.display_info()


class License:
    """
    Represents a driver's license with relevant information.

    Attributes:
        license_number (str): The unique license number.
        expiration_date (str): The date when the license expires.
    """

    def __init__(self, license_number, expiration_date):
        """
        Initializes a new License instance.

        Args:
            license_number (str): The unique license number.
            expiration_date (str): The date when the license expires.
        """
        self.license_number = license_number
        self.expiration_date = expiration_date

    def display_info(self):
        """
        Displays the license number and expiration date.
        """
        print(f"License Number: {self.license_number}")
        print(f"Expiration Date: {self.expiration_date}")


# if __name__ == "__main__":
#     driving_license = License("1545JGJH", "10-10-2030")
#     driving_license.display_info()