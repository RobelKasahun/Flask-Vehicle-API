from app.models import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    # class property
    vehicle = Vehicle(
        brand="Toyota",
        model="Camry",
        year=2020,
        engine_size=2.5,
        fuel_type="Gasoline",
        transmission="Automatic",
        mileage=35000,
        doors=4,
        owner_count=1,
        price=25000,
    )

    def test_brand(self):
        self.assertEqual(TestVehicle.vehicle.brand, "Toyota")

    def test_model(self):
        self.assertEqual(TestVehicle.vehicle.model, "Camry")

    def test_year(self):
        self.assertEqual(TestVehicle.vehicle.year, 2020)

    def test_engine_size(self):
        self.assertEqual(TestVehicle.vehicle.engine_size, 2.5)

    def test_fuel_type(self):
        self.assertEqual(TestVehicle.vehicle.fuel_type, "Gasoline")

    def test_transmission(self):
        self.assertEqual(TestVehicle.vehicle.transmission, "Automatic")

    def test_mileage(self):
        self.assertEqual(TestVehicle.vehicle.mileage, 35000)

    def test_owner_count(self):
        self.assertEqual(TestVehicle.vehicle.owner_count, 1)

    def test_price(self):
        self.assertEqual(TestVehicle.vehicle.price, 25000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
