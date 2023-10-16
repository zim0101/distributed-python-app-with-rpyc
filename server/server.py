import rpyc
from decorators import expose
from app import Car, Driver, License


# Define an RPyC service class
class DistributedAppService(rpyc.Service):
    def on_connect(self, conn):
        """
        This method is called when a client connects to the service. You can perform any setup or
        initialization here if needed.
        """
        pass

    def on_disconnect(self, conn):
        """
        This method is called when a client disconnects from the service. You can perform any cleanup
        or logging here if needed.
        """
        pass

    @expose
    def create_car_class(self, make, model, fuel_type, num_doors):
        """
        Exposes the create_car_class method to clients, allowing them to create Car objects.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            fuel_type (str): The fuel type of the car.
            num_doors (int): The number of doors the car has.

        Returns:
            Car: The created Car object.

        Example:
            import rpyc

            connection = rpyc.connect("localhost", 18861)
            car = connection.root.create_car_class("Ford", "Mustang", "Gasoline", 2)
            car.lock_doors()
        """
        car = Car(make, model, fuel_type, num_doors)
        return car

    @expose
    def create_driver_class(self, name, license_number, expiration_date):
        """
        Exposes the create_driver_class method to clients, allowing them to create Driver objects.

        Args:
            name (str): The name of the driver.
            license_number (str): The driver's license number.
            expiration_date (str): The expiration date of the driver's license.

        Returns:
            Driver: The created Driver object.

        Example:
            import rpyc

            connection = rpyc.connect("localhost", 18861)
            driver = connection.root.create_driver_class("Lewis Hamilton", "2373482JHGJHG", "01-01-2050")
            driver.show_driving_license_info()
        """

        driving_license = License(license_number, expiration_date)
        driver = Driver(name, driving_license)
        return driver


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    print("Starting server...")
    server = ThreadedServer(DistributedAppService, port=18861,
                            protocol_config={'allow_public_attrs': True, })
    server.start()
