class Dorms:
    def __init__(self, rooms = 10):
        self.rooms_num = rooms
        self.available_rooms = rooms

class Room:
    def __init__(self, beds = 8):
        self.beds = beds
        self.soldiers = []
        self.available_beds = self.beds - len(self.soldiers)

    def add_soldier(self, soldier):
        if len(self.soldiers) < self.beds:
            self.soldiers.append(soldier)
        else:
            return 'room is full'
        
    def get_available_beds(self):
        return self.available_beds
    

             