#-----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#-----------------------------------------------------------------------------
# Recreate the possible combinations of victories, ties, and defeats for
# each season by printing out the results and producing the results in the
# soccer-out.txt file by utilizing the data stored in the soccer-in.txt file.
#-----------------------------------------------------------------------------
# Data Generation Template
#-----------------------------------------------------------------------------
# 1 3
# 1 1
# 1 0
# 20 30
#-----------------------------------------------------------------------------
# Desired Output
#-----------------------------------------------------------------------------
# Season: 1, Games Played: 1, Points Earned: 3
# Possible Victory-Draw-Defeat Records
# ------------------------------------
# 1-0-0
#
# Season: 2, Games Played: 1, Points Earned: 1
# Possible Victory-Draw-Defeat Records
# ------------------------------------
# 0-1-0
#
#
# Season: 3, Games Played: 1, Points Earned: 0
# Possible Victory-Draw-Defeat Records
# ------------------------------------
# 0-0-1
#
# Season: 4, Games Played: 20, Points Earned: 30
# Possible Victory-Draw-Defeat Records
# ------------------------------------
# 10-0-10
# 9-3-8
# 8-6-6
# 7-9-4
# 6-12-2
# 5-15-0
#-----------------------------------------------------------------------------

def process_season(season, games_played, points_earned):
    
    print("Season: " + str(season) + ", Games Played: " +
          str(games_played) + ", Points Earned: " + str(points_earned))
    print("Possible Victory-Draw-Defeat Records")
    print("------------------------------------")

    x = points_earned / 3
    
    for i in range(int(x), 0, -1):
        y = points_earned - i*3
        z = games_played - (i+y)
        if (i + y + z <= games_played) and (z >= 0):
            print(str(i) + "-" + str(y) + "-" + str(z))

    if (x < 1) and (x != 0):
        x = points_earned
        print("0-" + str(x) + "-" + str(games_played - x))
    
    if (x == 0):
        print("0-0-" + str(games_played) + "\n")

# Let x represent the number of games that result in a victory.
# Let y represent the number of games that result in a draw.
# Let z represent the number of games that result in a defeat.

def process_seasons(seasons):
    for i in range(len(seasons)):
        the_season = seasons[i]
        process_season(i+1, the_season[0], the_season[1])

association_football_seasons = ([1, 3], [1, 1], [1, 0], [20, 30])
process_seasons(association_football_seasons)

#----------------------------------------------------------------------------------

# Change 01: The process_season parameters also include output_file.
print("\nChange 01: The process_season parameters also include output_file.\n")

def process_season(output_file, season, games_played, points_earned):
    
    output_file.write("Season: " + str(season) + ", Games Played: " + str(games_played)
                      + ", Points Earned: " + str(points_earned) + "\n")
    output_file.write("Possible Victory-Draw-Defeat Records\n")
    output_file.write("------------------------------------\n")

    x = points_earned / 3
    for i in range(int(x), 0, -1):
        y = points_earned - (i*3)
        z = games_played - (i+y)
        if (i + y + z <= games_played) and (z >= 0):
            output_file.write(str(i) + "-" + str(y) + "-" + str(z) + "\n")

    if (x < 1) and (x != 0):
        x = points_earned
        output_file.write("0-" + str(x) + "-" + str(games_played - x) + "\n")

    if (x == 0):
        output_file.write("0-0-" + str(games_played) + "\n")
    output_file.write("\n")

# Change 02: The process_seasons parameters are input_file (soccer-in.txt) and output_file(soccer-out.txt).
print("Change 02: The process_seasons parameters are input_file(soccer-in.txt) and output_file(soccer-out.txt).\n")

def process_seasons(input_file, output_file):
    input_file = open(input_file, "r")
    output_file = open(output_file, "w")
    season_number = 1

    for season in input_file:
        season = season.split()
        games_played = int(season[0])
        points_earned = int(season[1])
        process_season(output_file, season_number, games_played, points_earned)
        season_number = season_number + 1

# Change 03: The function process_seasons is called with soccer-in.txt and soccer-out.txt.
print("Change 03: The function process_seasons is called with soccer-in.txt and soccer-out.txt.\n")

process_seasons("soccer-in.txt", "soccer-out.txt")
