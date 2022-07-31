from bs4 import BeautifulSoup
import requests
def getData(team, player):
    box_scores = []
    third_plays = []

    gamesPlayed = []

    url = ""

    if (team == "BKN" or team == "WSH"):
        url = f"https://www.basketball-reference.com/teams/{team}/2022/gamelog/"
        print(url)
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        
        reg_season_table = doc.find_all("td", class_ = "left")
        
        for row in reg_season_table:
            res = row.find_all("a")
            if("boxscores" in res[0]['href']):
                box_scores.append(res[0]['href'])
            
    else:
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

    return (third_plays, gamesPlayed.count(True))