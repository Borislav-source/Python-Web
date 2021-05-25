from appliances.appliance import Appliance


class Fridge(Appliance):
    initial_cost = 1.2

    def __init__(self):
        super().__init__(cost = self.initial_cost)
