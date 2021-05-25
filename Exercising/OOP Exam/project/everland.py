class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumption = 0
        for room in self.rooms:
            consumption += room.calculate_expenses(room.appliances, room.children) + room.room_cost
        return f"Monthly consumption: {consumption:.2f}$."

    def pay(self):
        for room in self.rooms:
            costs = room.calculate_expenses(room.appliances, room.children) + room.room_cost
            if room.budget < costs:
                print(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
            else:
                print(f"{room.family_name} paid {room.expenses+room.room_cost:.2f}$ and have {room.budget:.2f}$ left.")

    def _get_population(self):
        population = 0
        for room in self.rooms:
            population += room.members_count
        return population

    def status(self):
        print(f'Total population: {self._get_population()}')
        for room in self.rooms:
            print(f'{room.family_name} with {room.members_count} members. Budget: {room.budget - room.expenses - room.room_cost}$, Expenses: {room.expenses}$')
            for child in room.children:
                print(f"--- Child {room.children.index(child) + 1} monthly cost: {child.get_monthly_expenses():.2f}$")
            print(f"--- Appliances monthly cost: {room.expenses}$")
