import rpyc


def main():
    connection = rpyc.connect("localhost", 18861)

    car = connection.root.create_car_class("Ford", "Mustang", "Gasoline", 2)
    car.lock_doors()
    car.start_engine()
    car.stop_engine()
    car.unlock_doors()

    driver = connection.root.create_driver_class("Lewis Hamilton", "2373482JHGJHG", "01-01-2050")
    driver.show_driving_license_info()
    driver.driving_license.display_info()


if __name__ == "__main__":
    main()
