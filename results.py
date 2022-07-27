from parse import getAssists, getBlocks, getSteals, getTurnovers, getFouls, getTotalMinutes
from parse1 import get2Makes, get2Misses, get3Makes, get3Misses, getFTMakes, getFTMisses, getDRob, getORob

twopoints_made = get2Makes();
twopoints_missed = get2Misses();
threepoints_made = get3Makes();
threepoints_missed = get3Misses()
freethrows_made = getFTMakes()
freethrows_missed = getFTMisses()
orob = getORob()
drob = getDRob()
assist = getAssists()
block = getBlocks()
steal = getSteals()
turnover = getTurnovers()
fouls = getFouls()
gamesPlayed = getTotalMinutes()

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

print(f"Points: {total_points / gamesPlayed}")
print()

print(f"Assist: {total_assists / gamesPlayed}")
print()

print(f"2 point percentage: {two_point_percentage}")
print()

print(f"3 point percentage: {three_point_percentage}")
print()

print(f"Shooting percentage: {shooting_percentage}")
print()

print(f"FT point percentage: {freethrow_percentage}")
print()

print(f"Rebounds: {total_rebounds / gamesPlayed} total, {orob / gamesPlayed} offensive, {drob / gamesPlayed} defensive")
print()

print(f"Blocks: {total_blocks / gamesPlayed}")
print()

print(f"Steals: {total_steals / gamesPlayed}")
print()

print(f"Turnovers: {total_turnovers / gamesPlayed}")
print()

print(f"Fouls: {total_fouls / gamesPlayed}")
print()