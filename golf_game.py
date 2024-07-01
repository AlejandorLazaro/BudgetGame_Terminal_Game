import random

# Directional number constants
NORTH = 0
SOUTH = 1

class Player:
    def __init__(self, name, age, handicap, position=0, starting_stroke_count=0):
        self.name = name
        self.age = age
        self.handicap = handicap
        self.favorite_club = None
        self.favorite_course = None
        self.bag = []
        self.position = position
        self.direction_to_hole = NORTH
        self.stroke_count = starting_stroke_count

    def get_better(self, improvement):
        self.handicap -= improvement
        if self.handicap < 0:
            self.handicap = 0
        print(f"{self.name}'s handicap has improved! Current handicap is {self.handicap}.")
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
        repr_str = f"{self.name} is {self.age} years of age and they are a {self.handicap} handicap."
        if self.favorite_club:
                repr_str += f"\n{self.name}: My {self.favorite_club.name} is my favorite club!"
        if self.favorite_course:
                repr_str += f"\n{self.name}: '{self.favorite_course}' is my favorite course!"
        return repr_str

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
        return f"I have a {self.name} club, it's a {self.brand} and it goes {self.yards} yards!"

class Wind:
    def __init__(self):
        self.min_speed = 0
        self.max_speed = 5
        self.curr_speed = random.randint(self.min_speed, self.max_speed)
        self.direction = random.choice([NORTH, SOUTH])
        self.starting_change_chance = .3
        self.curr_change_chance = .3
        self.rounds_since_last_change = 0
        self.chance_incr_per_unchanging_round = .05

    def update_wind(self):
        if random.random() > (self.curr_change_chance + (self.rounds_since_last_change * self.chance_incr_per_unchanging_round)):
            self.direction = random.choice([NORTH, SOUTH])
            self.curr_speed = random.randint(self.min_speed, self.max_speed)
            self.rounds_since_last_change = 0
        else:
            self.rounds_since_last_change += 1


class GolfGame:
    curr_round = 1

    def __init__(self, hole_dist=0, wind_enabled=False):
        # Initialize game environment values

        # Ensure random elements can be replicated based on a seed for future debugging
        # (i.e., wind direction and strength, ball roll distance, terrain slopes, etc)
        # self.seed = 1234
        # random.seed(self.seed)
        # With the above seed, we get:
        # * Wind of 0, 5N...
        # * Hole starting distance of 375
        # * Win in 2 strokes with 300->73
        random.seed()  # Comment the above and uncomment this to have random gameplay

        self.hole_distance = hole_dist or random.randint(150, 500)

        self.wind_enabled = wind_enabled
        if self.wind_enabled:
            self.wind = Wind()

        # Initialize player(s)
        self.player = Player("Stef", 29, 21.7)
        # Set the player direction, since it's possible the player is past the hole starting out
        self.update_player_direction()
        print(self.player)


        club1 = Club("Driver", "Ping", 300)
        club2 = Club("Gap Wedge", "Mizuno", 134)
        club3 = Club("3-Wood", "Ping", 236)
        #Adding clubs to self.player's bag
        self.player.add_club_to_bag(club1)
        self.player.add_club_to_bag(club2)
        self.player.add_club_to_bag(club3)

        #Listing clubs in self.player's bag
        # print(self.player.list_clubs_in_bag())

        #Print club objects directly to see the __repr__ output
        # print(club1)
        # print(club2)
        # print(club3)

        # Configure player values (handicaps, favorite courses, starting club, etc)
        self.player.get_better(2)

        self.player.set_favorite_club(club2)

        self.player.set_favorite_course("Mo Willie")

        print(self.player)

    def start_game(self):
        print(
            self.ascii_header() +
            f"Welcome to GOLF GAME! The hole is currently {self.hole_distance} yards away towards the north."
            )

    def game_loop(self):
        print(f"\n####################\nCurrent round is {self.curr_round}.")
        self.print_course_env()
        while self.player.position != self.hole_distance:

            try:
                shot_distance = int(input("Choose the distance of your shot (1 to 300 yards): "))
                if 1 <= shot_distance <= 300:
                    self.calculate_shot_distance_traveled(shot_distance)
                else:
                    print("Please enter a distance between 1 and 300 yards.")
                    continue
            except ValueError:
                print('Please enter a valid number')
                continue

            # Exit early if we won the game
            if self.player.position == self.hole_distance:
                break

            self.update_player_direction()
            self.update_course_env()
            self.curr_round += 1
            print(f"\n####################\nCurrent round is {self.curr_round}.")
            self.print_course_env()

        print(f"\n\nCongratulations! You reached the hole in {self.player.stroke_count} strokes.")

    def calculate_shot_distance_traveled(self, shot_distance):
        if self.wind_enabled:
            air_factor = shot_distance / 21
            wind_distance_mod = random.randint(0, int(air_factor * self.wind.curr_speed))
            if wind_distance_mod > 0:
                print(
                    f"༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄\n"
                    f"The wind takes over! The ball distance has shifted!\n"
                    f"༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄ ༄༄ ༄༄༄"
                )
                if self.player.direction_to_hole == self.wind.direction:
                    shot_distance += wind_distance_mod
                else: shot_distance -= wind_distance_mod

        if self.player.direction_to_hole == NORTH:
            self.player.position += shot_distance
        if self.player.direction_to_hole == SOUTH:
            self.player.position -= shot_distance
        self.player.stroke_count += 1

        dir_str = "south" if self.player.direction_to_hole else "north"
        print(f"You hit the ball {shot_distance} yards towards the {dir_str}.\nYour total distance is now {self.player.position} yards. The hole is now {abs(self.hole_distance - self.player.position)} yards away.")

    def update_player_direction(self):
        player_switched_dir = False

        # If the player is facing North, but they are past the hole, they should swap to face South
        if self.player.direction_to_hole == NORTH and self.player.position - self.hole_distance > 0:
            self.player.direction_to_hole = SOUTH
            player_switched_dir = True

        # If the player is facing South, but the hole is further than they are, swap to face North
        elif self.player.direction_to_hole == SOUTH and self.hole_distance - self.player.position > 0:
            self.player.direction_to_hole = NORTH
            player_switched_dir = True

        if player_switched_dir:
            print(f"Your shot went {abs(self.player.position - self.hole_distance)} yards past the hole. You need to hit the ball back.")


    def update_course_env(self):
        if self.wind_enabled:
            self.wind.update_wind()

    def print_course_env(self):
        if self.wind_enabled:
            if self.wind.curr_speed == 0:
                print(f"The wind has died down...")
            else:
                dir_str = "south" if self.wind.direction else "north"
                print(f"A wind blows towards the {dir_str} at {self.wind.curr_speed} mph...")

    def ascii_header(self):
        return (
            f"\n"
            f"   ___           .   ,__         ___                           \n"
            f" .'   \    __.   |   /  `      .'   \    ___  , _ , _     ___  \n"
            f" |       .'   \  |   |__       |        /   ` |' `|' `. .'   ` \n"
            f" |    _  |    |  |   |         |    _  |    | |   |   | |----' \n"
            f"  `.___|  `._.' /\__ |          `.___| `.__/| /   '   / `.___, \n"
            f"\n"
            f"|        '\                   .  .                             |\n"
            f"|          \              .         ' .                        |\n"
            f"|         O>>         .                 'o                     |\n"
            f"|          \       .                                           |\n"
            f"|          /\    .                                             |\n"
            f"|         / /  .'                                              |\n"
            f" ^^^^^^^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n"
        )