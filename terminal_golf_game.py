import argparse
import golf_game

def check_start_pos_value(value):
    ivalue = int(value)
    if ivalue < 0 or ivalue > 500:
        raise argparse.ArgumentTypeError(f"{ivalue} is outside of the acceptable range of 0 to 500 for the player start.")
    return ivalue

def parse_args():
    parser = argparse.ArgumentParser()
    # Set 'required' to False to get the DEFAULT_LIST_OF_STORED_JOBS
    parser.add_argument('--wind', action='store_true', dest='wind_enabled',
        help='Enable wind during this game. Off by default.')
    # TODO: Starting position logic on player instantiation and logging to terminal
    # parser.add_argument('--start_pos', type=check_start_pos_value, default=0, dest='start_pos',
    #     help='Starting position of the player in yards in the Northerly direction. Defaults to 0.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    game = golf_game.GolfGame(wind_enabled=args.wind_enabled)

    game.start_game()
    game.game_loop()

if __name__ == "__main__":
    main()