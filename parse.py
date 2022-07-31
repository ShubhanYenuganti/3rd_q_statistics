from input import getTeam, getPlayer
from access import getData
player = getPlayer()
team = getTeam()

data = getData(team, player)
third_plays = data[0]
total_games = data[1]

third_player_plays = []

# Filter plays by player
for elem in third_plays:
    if player in elem:
        third_player_plays.append(elem)
    else:
        continue

def getScorePlays():
    # Filter scoring plays
    score = []
    for elem in third_player_plays:
        if (player + " makes") in elem:
            score.append(elem)
        else:
            continue 
    return score

def getMissPlays():
    # Filter misses
    miss = []
    for elem in third_player_plays:
        if (player + " misses") in elem:
            miss.append(elem)
        else:
            continue
    return miss

def getAssists():
    # Filter assists
    assist = []
    for elem in third_player_plays:
        if ("assist by " + player) in elem:
            assist.append(elem)
        else:
            continue
    return assist

def getRebounds():
    # Filter rebound
    rebound = []
    for elem in third_player_plays:
        if ("rebound by " + player) in elem:
            rebound.append(elem)
        else:
            continue
    return rebound


def getBlocks():
    # Filter block
    block = []
    for elem in third_player_plays:
        if ("block by " + player) in elem:
            block.append(elem)
        else:
            continue
    return block

def getSteals():
    # Filter steal
    steal = []
    for elem in third_player_plays:
        if ("steal by " + player) in elem:
            steal.append(elem)
        else:
            continue
    return steal

def getTurnovers():
    # Filter turnover
    turnover = []
    for elem in third_player_plays:
        if ("Turnover by " + player) in elem:
            turnover.append(elem)
        else:
            continue
    return turnover

def getFouls(): 
    # Filter fouls
    fouls = []
    for elem in third_player_plays:
        if ("foul by " + player) in elem:
            fouls.append(elem)
        else:
            continue
    return fouls

def getTotalMinutes():
    return total_games

def getPlayerName():
    return player;