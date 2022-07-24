from bs4 import BeautifulSoup
import requests

box_scores = []
third_plays = []
player_third_plays = []

score = []
miss = []
assist = []
rebound = []
block = []
steal = []
turnover = []
fouls = []
freethrowmade = []
freethrowmissed = []

twopoints_made = 0;
twopoints_missed = 0;
threepoints_made = 0;
threepoints_missed = 0;
freethrows_made = 0;
freethrows_missed = 0;
orob = 0;
drob = 0;

gamesPlayed = []

player = input("Which player do you want to look at? (Ex: S. Curry) ");

team = input("Which player do you want to look at? Ex: type (GSW) ");
url = f"https://www.basketball-reference.com/teams/{team}/2022_games.html"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

reg_season_table = doc.find("div", {"id": "div_games"})
items = reg_season_table.find_all("a", text = "Box Score", href = True)

for item in items:
    box_scores.append(item['href'])

for b in box_scores:
    box_url = f"https://www.basketball-reference.com{b}"
    play_url = box_url[0:46] + "/pbp/" + box_url[46:]
    play_page = requests.get(play_url).text
    play_doc = BeautifulSoup(play_page, "html.parser")

    table = play_doc.find("table")
    start_q_3 = table.find("td", text = "Start of 3rd quarter")
    q_3 = start_q_3.find_all_next("td")

    player_played = False

    for row in q_3:
        if (row.text.strip() != "End of 3rd quarter"):
            third_plays.append(row.text.strip())
        else:
            break

        if player in row.text.strip():
            player_played = True
        else:
            continue;
    
    gamesPlayed.append(player_played);

# Filter plays by player
for elem in third_plays:
    if player in elem:
        player_third_plays.append(elem)
    else:
        continue

# Add to corresponding array   
# Filter scoring plays
for elem in player_third_plays:
    if (player + " makes") in elem:
        score.append(elem)
    else:
        continue

# Filter misses
for elem in player_third_plays:
    if (player + " misses") in elem:
        miss.append(elem)
    else:
        continue

# Filter assists
for elem in player_third_plays:
    if ("assist by " + player) in elem:
        assist.append(elem)
    else:
        continue

# Filter rebound
for elem in player_third_plays:
    if ("rebound by " + player) in elem:
        rebound.append(elem)
    else:
        continue

# Filter block
for elem in player_third_plays:
    if ("block by " + player) in elem:
        block.append(elem)
    else:
        continue

# Filter steal
for elem in player_third_plays:
    if ("steal by " + player) in elem:
        steal.append(elem)
    else:
        continue

# Filter turnover
for elem in player_third_plays:
    if ("Turnover by " + player) in elem:
        turnover.append(elem)
    else:
        continue

# Filter fouls
for elem in player_third_plays:
    if ("foul by " + player) in elem:
        fouls.append(elem)
    else:
        continue

# Total 2 points made
for elem in score:
    if ("makes 2-pt") in elem:
        twopoints_made += 1
    else:
        continue

# Total 2 points missed
for elem in miss:
    if ("misses 2-pt") in elem:
        twopoints_missed += 1
    else:
        continue

# Total 3 points made
for elem in score:
    if ("makes 3-pt") in elem:
        threepoints_made += 1
    else:
        continue

# Total 2 points missed
for elem in miss:
    if ("misses 3-pt") in elem:
        threepoints_missed += 1
    else:
        continue

# Total FT made
for elem in score:
    if ("makes free throw") in elem:
            freethrows_made += 1
    else:
        continue

# Account for technicals
for elem in score:
    if ("makes technical free throw") in elem:
            freethrows_made += 1
    else:
        continue

# Total fts missed
for elem in miss:
    if ("misses free throw") in elem:
            freethrows_missed += 1
    else:
        continue

# Account for technicals
for elem in score:
    if ("misses technical free throw") in elem:
            freethrows_missed += 1
    else:
        continue

# Total offensive boards
for elem in rebound:
    if ("Offensive") in elem:
        orob += 1
    else:
        continue

# Total defensive board
for elem in rebound:
    if ("Defensive") in elem:
        drob += 1
    else:
        continue

total_points = twopoints_made * 2 + threepoints_made * 3 + freethrows_made;

if (twopoints_made != 0):
    two_point_percentage = (twopoints_made / (twopoints_missed + twopoints_made)) * 100;
else:
    two_point_percentage = 0

if (threepoints_made != 0):
    three_point_percentage = (threepoints_made / (threepoints_missed + threepoints_made)) * 100;
else:        
    three_point_percentage = 0

if ((twopoints_made+threepoints_made) != 0):
    shooting_percentage = ((twopoints_made+threepoints_made) / (twopoints_missed+threepoints_missed + (twopoints_made+threepoints_made))) * 100;
else:
    shooting_percentage = 0

if (freethrows_made != 0):
    freethrow_percentage = (freethrows_made / (freethrows_missed + freethrows_made)) * 100;
else:
    freethrow_percentage = 0;

total_assists = len(assist)
total_rebounds = orob + drob;
total_blocks = len(block)
total_steals = len(steal)
total_turnovers = len(turnover)
total_fouls = len(fouls)
total_games_played = gamesPlayed.count(True)

print(f"Points: {total_points}")
print()

print(f"Assist: {total_assists}")
print()

print(f"2 point percentage: {two_point_percentage}")
print()

print(f"3 point percentage: {three_point_percentage}")
print()

print(f"Shooting percentage: {shooting_percentage}")
print()

print(f"FT point percentage: {freethrow_percentage}")
print()

print(f"Rebounds: {total_rebounds} total, {orob} offensive, {drob} defensive")
print()

print(f"Blocks: {total_blocks}")
print()

print(f"Steals: {total_steals}")
print()

print(f"Turnovers: {total_turnovers}")
print()

print(f"Fouls: {total_fouls}")
print()

print('------------------------------------')
print('Per reg season game')
print()

print(f"Points: {total_points / total_games_played}")
print()

print(f"Assist: {total_assists / total_games_played}")
print()

print(f"2 point percentage: {two_point_percentage}")
print()

print(f"3 point percentage: {three_point_percentage}")
print()

print(f"Shooting percentage: {shooting_percentage}")
print()

print(f"FT point percentage: {freethrow_percentage}")
print()

print(f"Rebounds: {total_rebounds / total_games_played} total, {orob / total_games_played} offensive, {drob / total_games_played} defensive")
print()

print(f"Blocks: {total_blocks / total_games_played}")
print()

print(f"Steals: {total_steals / total_games_played}")
print()

print(f"Turnovers: {total_turnovers / total_games_played}")
print()

print(f"Fouls: {total_fouls / total_games_played}")
print()