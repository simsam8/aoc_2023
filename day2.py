from input_template import get_input


content = get_input()


total_reds = 12
total_greens = 13
total_blues = 14


def create_color_map(color_set):
    color_set = [color.split(" ") for color in color_set]
    color_set = {bag[1]: int(bag[0]) for bag in color_set}
    return color_set


def format_color_set(sets):
    sets = sets.split("; ")
    sets = [bag.split(", ") for bag in sets]
    sets = [create_color_map(bag) for bag in sets]
    return sets


def game_is_valid(game):
    for bag in game[1]:
        try:
            if bag["blue"] > total_blues:
                game[2] = "invalid"
                return game
        except:
            pass

        try:
            if bag["red"] > total_reds:
                game[2] = "invalid"
                return game
        except:
            pass

        try:
            if bag["green"] > total_greens:
                game[2] = "invalid"
                return game
        except:
            pass

    game[2] = "valid"
    return game


def minimum_cubes_power(game):
    highest_red = -1
    highest_green = -1
    highest_blue = -1
    for bag in game[1]:
        try:
            if bag["blue"] > highest_blue:
                highest_blue = bag["blue"]
        except:
            pass

        try:
            if bag["red"] > highest_red:
                highest_red = bag["red"]
        except:
            pass

        try:
            if bag["green"] > highest_green:
                highest_green = bag["green"]
        except:
            pass
    game[2] = highest_red * highest_green * highest_blue
    return game


def possible_games(games):
    games = [game_is_valid(game) for game in games]

    answer = 0

    for game in games:
        if game[2] == "valid":
            answer += game[0]

    print(answer)


def fewest_number_of_cubes(games):
    games = [minimum_cubes_power(game) for game in games]

    answer = 0

    for game in games:
        answer += game[2]

    print(answer)


games = []
for i, game in enumerate(content):
    sets = game[game.find(":") + 2 :]
    sets = format_color_set(sets)
    games.append([i + 1, sets, None])


# Part one
possible_games(games)

# Part two
fewest_number_of_cubes(games)
