from appliances.appliance import Appliance


class TV(Appliance):
    initial_cost = 1.5

    def __init__(self):
        super().__init__(cost=self.initial_cost)
