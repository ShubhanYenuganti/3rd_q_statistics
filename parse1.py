from parse import getScorePlays, getMissPlays, getRebounds

score = getScorePlays();
miss = getMissPlays();
rebound = getRebounds();

def get2Makes():
    twopoints_made = 0
    # Total 2 points made
    for elem in score:
        if ("makes 2-pt") in elem:
            twopoints_made += 1
        else:
            continue
    return twopoints_made

def get2Misses():
    twopoints_missed = 0
    for elem in miss:
        if ("misses 2-pt") in elem:
            twopoints_missed += 1
        else:
            continue
    return twopoints_missed

def get3Makes():
    # Total 3 points made
    threepoints_made = 0
    for elem in score:
        if ("makes 3-pt") in elem:
            threepoints_made += 1
        else:
            continue
    return threepoints_made

def get3Misses():
    # Total 3 points missed
    threepoints_missed = 0
    for elem in miss:
        if ("misses 3-pt") in elem:
            threepoints_missed += 1
        else:
            continue

    return threepoints_missed

def getFTMakes():
    # Total FT made
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

def getFTMisses():
    # Total fts missed
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

def getORob():
    orob = 0
    # Total offensive boards
    for elem in rebound:
        if ("Offensive") in elem:
            orob += 1
        else:
            continue
    return orob

def getDRob():
    # Total defensive board
    drob = 0
    for elem in rebound:
        if ("Defensive") in elem:
            drob += 1
        else:
            continue
    return drob

