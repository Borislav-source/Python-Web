from appliances.appliance import Appliance


class Stove(Appliance):
    initial_cost = 0.7

    def __init__(self):
        super().__init__(cost=self.initial_cost)
