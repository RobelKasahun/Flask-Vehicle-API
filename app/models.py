class Vehicle(object):
    def __init__(
        self,
        brand,
        model,
        year,
        engine_size,
        fuel_type,
        transmission,
        mileage,
        doors,
        owner_count,
        price,
    ):
        """Vehicle initializer"""
        self._brand = brand
        self._model = model
        self._year = year
        self._engine_size = engine_size
        self._fuel_type = fuel_type
        self._transmission = transmission
        self._mileage = mileage
        self._doors = doors
        self._owner_count = owner_count
        self._price = price

    """ Setters and Getters"""

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def engine_size(self):
        return self._engine_size

    @engine_size.setter
    def engine_size(self, engine_size):
        self._engine_size = engine_size

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        self._fuel_type = fuel_type

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, transmission):
        self._transmission = transmission

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, doors):
        self._doors = doors

    @property
    def owner_count(self):
        return self._owner_count

    @owner_count.setter
    def owner_count(self, owner_count):
        self._owner_count = owner_count

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
