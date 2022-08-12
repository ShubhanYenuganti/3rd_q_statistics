from parse import getScorePlays, getMissPlays, getRebounds

score = getScorePlays();
miss = getMissPlays();
rebound = getRebounds();

# Total 2 points made
def get2Makes():
    twopoints_made = 0
    for elem in score:
        if ("makes 2-pt") in elem:
            twopoints_made += 1
        else:
            continue
    return twopoints_made

# Total 2 points missed
def get2Misses():
    twopoints_missed = 0
    for elem in miss:
        if ("misses 2-pt") in elem:
            twopoints_missed += 1
        else:
            continue
    return twopoints_missed

# Total 3 points made
def get3Makes():
    threepoints_made = 0
    for elem in score:
        if ("makes 3-pt") in elem:
            threepoints_made += 1
        else:
            continue
    return threepoints_made

# Total 3 points missed
def get3Misses():
    threepoints_missed = 0
    for elem in miss:
        if ("misses 3-pt") in elem:
            threepoints_missed += 1
        else:
            continue

    return threepoints_missed

# Total FT made
def getFTMakes():
    freethrows_made = 0
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
    return freethrows_made
# Total fts missed
def getFTMisses():
    freethrows_missed = 0
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
    return freethrows_missed
# Total offensive boards
def getORob():
    orob = 0
    for elem in rebound:
        if ("Offensive") in elem:
            orob += 1
        else:
            continue
    return orob
    
# Total defensive boards
def getDRob():
    drob = 0
    for elem in rebound:
        if ("Defensive") in elem:
            drob += 1
        else:
            continue
    return drob

