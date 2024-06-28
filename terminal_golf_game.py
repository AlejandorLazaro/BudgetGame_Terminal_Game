import random

def golf_game():
    hole_distance = random.randint(150, 500)
    player_position = 0
    stroke_count = 0

    print(f"Welcome to GOLF GAME! The hole is currently {hole_distance} yards away.")

    while player_position < hole_distance:
        try:
            shot_distance = int(input("Choose the distance of your shot (1 to 300 yards): "))
            if 1 <= shot_distance <= 300:
                player_position += shot_distance
                stroke_count += 1
                print(f"You hit the ball {shot_distance} yards. Your total distance is now {player_position} yards.")
            else:
                print("Please enter a distance between 1 and 300 yards.")
        except ValueError:
            print('Please enter a valud number')
        
        if player_position > hole_distance:
            print(f"Your shot went {player_position - hole_distance} yards past the hole. You need to hit the ball back.")

            player_position = hole_distance - (player_position - hole_distance)

        
        print(f"Congratulations! You reached the hole in {stroke_count} strokes.")

golf_game()