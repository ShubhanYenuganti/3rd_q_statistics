from input import getTeam, getPlayer
from access import getData
player = getPlayer()
team = getTeam()

data = getData(team, player)
third_plays = data[0]
total_games = data[1]

third_player_plays = []

# Filters game log to plays made by player
for elem in third_plays:
    if player in elem:
        third_player_plays.append(elem)
    else:
        continue

# Filter scoring plays
def getScorePlays():
    score = []
    for elem in third_player_plays:
        if (player + " makes") in elem:
            score.append(elem)
        else:
            continue 
    return score

# Filter misses
def getMissPlays():
    miss = []
    for elem in third_player_plays:
        if (player + " misses") in elem:
            miss.append(elem)
        else:
            continue
    return miss

# Filter assists
def getAssists():
    assist = []
    for elem in third_player_plays:
        if ("assist by " + player) in elem:
            assist.append(elem)
        else:
            continue
    return assist

# Filter rebound
def getRebounds():
    rebound = []
    for elem in third_player_plays:
        if ("rebound by " + player) in elem:
            rebound.append(elem)
        else:
            continue
    return rebound

# Filter blocks
def getBlocks():
    block = []
    for elem in third_player_plays:
        if ("block by " + player) in elem:
            block.append(elem)
        else:
            continue
    return block

# Filter steals
def getSteals():
    steal = []
    for elem in third_player_plays:
        if ("steal by " + player) in elem:
            steal.append(elem)
        else:
            continue
    return steal

# Filter turnovers
def getTurnovers():
    turnover = []
    for elem in third_player_plays:
        if ("Turnover by " + player) in elem:
            turnover.append(elem)
        else:
            continue
    return turnover

# Filter fouls
def getFouls(): 
    fouls = []
    for elem in third_player_plays:
        if ("foul by " + player) in elem:
            fouls.append(elem)
        else:
            continue
    return fouls

def getGamesPlayed():
    return total_games

def getPlayerName():
    return player;