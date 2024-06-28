class Player:
    def __init__(self, name, age, handicap):
        self.name = name
        self.age = age
        self.handicap = handicap
        self.favorite_club = None
        self.favorite_course = None
        self.bag = []

    def get_better(self, improvement):
        self.handicap -= improvement
        if self.handicap < 0:
            self.handicap = 0
        return self.handicap

    def set_favorite_club(self, club):
        self.favorite_club = club

    def get_favorite_club(self):
        return self.favorite_club

    def set_favorite_course(self, course):
        self.favorite_course = course

    def get_favorite_course(self):
        return self.favorite_course
    
    def add_club_to_bag(self, club):
        self.bag.append(club)

    def list_clubs_in_bag(self):
        return [club.name for club in self.bag]
    
    def __repr__(self) -> str:
        return "{name} is {age} years of age and they are a {handicap} handicap".format(name = self.name, age = self.age, handicap = self.handicap)


class Club:
    def __init__(self, name, brand, yards):
        self.name = name
        self.brand = brand
        self.yards = yards

    def use_club(self, force):
        distance = self.yards * force
        return distance

    def club_details(self):
        return f"Club: {self.name}, Brand: {self.brand}, Yards: {self.yards}"
    
    def __repr__(self) -> str:
        return "My {name} is my favorite club, it's a {brand} and it goes {yards} yards!".format(name = self.name, brand = self.brand, yards = self.yards)


player1 = Player("Stef", 29, 21.7)
print(player1)

club1 = Club("Driver", "Ping", 300)
club2 = Club("Gap Wedge", "Mizuno", 134)
club3 = Club("3-Wood", "Ping", 236)
#Adding clubs to player's bag
player1.add_club_to_bag(club1)
player1.add_club_to_bag(club2)
player1.add_club_to_bag(club3)

#Listing clubs in player's bag
print(player1.list_clubs_in_bag())

#Print club objects directly to see the __repr__ output
print(club1)
print(club2)

player1.get_better(2)
print(player1.handicap)

player1.set_favorite_club(club2)
print(player1.get_favorite_club().name)

player1.set_favorite_course("Mo Willie")
print(player1.get_favorite_course())

print(club1.use_club(1))

