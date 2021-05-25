from appliances.appliance import Appliance


class Laptop(Appliance):
    initial_cost = 1

    def __init__(self):
        super().__init__(cost=self.initial_cost)
