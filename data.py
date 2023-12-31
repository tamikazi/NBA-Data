import pandas as pd

years = range(2003, 2023)

player_pergame = {}
for y in years:
    year = y
    player_pergame["url" + str(y)] = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"


season_from = 2003
season_to = 2004

pl_pergame = {}

for i in player_pergame:
    pl_pergame["pl" + str(season_from + 1)] = pd.read_html(player_pergame[i])[0]
    pl_pergame["pl" + str(season_from + 1)]['Season'] = str(season_from)+'-'+str(season_to)

    season_from += 1
    season_to += 1

print(pl_pergame)