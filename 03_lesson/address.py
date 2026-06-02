class Address:

    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        self.addres = (
            f"{self.index}, {self.city}, "
            f"{self.street}, {self.house} - {self.apartment}"
        )
        return self.addres
