#the team name
team = "Toronto Blue Jays"
#the date at which the data is currently valid
date_of_data = "July 18, 2021"
#who the player is
player = "ladimir Guerrero Jr."
#how many home runs he has up to July 18, 2021
home_runs_to_date = 31
#total games he has played up to July 18, 2021
games_played = 88
#total games in a season
total_season_games = 162
#the record for the home runs
home_run_record = 73

#calculating how many games are left in the season
games_remaining = total_season_games - games_played
#the average number of homeruns for the player
home_runs_per_game = home_runs_to_date/games_played
#the prediction for how many home runs there will be according to the current average.
projected_home_runs = home_runs_per_game*total_season_games
#If the players probability/predicted amount of home runs is greater than the current record, then he breaks the record.
can_break_record = projected_home_runs> home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {date_of_data}")
print(f"the current MLB record for most home runs in a season is {home_run_record}")
print(f"with {games_remaining} games remaining and an average of {round(home_runs_per_game)}")
print(f'it is {can_break_record} that he is on pace to break the record')
print(f'{player} is projected to hit {round(projected_home_runs)} home runs this season.')


#The code has 2 lines of empty code for organization purposes, to differentiate between different sections:
#The given variables or data
#The variables that need to calculated according to the data given
#The code

#Without knowing the stored values in the variables, I know that games_remaining = total_season_games - games_played is correct because it takes the total season games and subtracts the games already played, leaving the remainder of the games in the season.