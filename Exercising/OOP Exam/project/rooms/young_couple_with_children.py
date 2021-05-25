from appliances.fridge import Fridge
from appliances.laptop import Laptop
from appliances.stove import Stove
from appliances.tv import TV
from rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=2)
        self.appliances = [TV(), Fridge(), Laptop()]
        self.children = list(children)
        self.members_count += len(self.children)

