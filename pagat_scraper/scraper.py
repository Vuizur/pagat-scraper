from dataclasses import dataclass, field
from bs4 import BeautifulSoup
import httpx
import pandas as pd

GET_RULES = False


def scrape_game_page(url: str) -> str:
    # Get all text from mainContent clearfix div
    r = httpx.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    maincontent = soup.find("div", {"class": "mainContent clearfix"})

    return str(maincontent)


@dataclass
class Game:
    name: str
    url: str
    players: str
    design: str
    quantity: str
    aliases: list[str] = field(default_factory=list)
    rules: str = ""
    bgg_ranking: float | None = None
    gameweight: float | None = None
    ranking: int | None = None


def add_bgg_rankings(games: list[Game]):
    # Load games.csv from BGG
    bgg_games = pd.read_csv("games.csv", index_col="BGGId")
    print(bgg_games)

    for game in games:
        try:
            bgg_id = bgg_games.loc[bgg_games["Name"] == game.name].index[0]
            game.bgg_ranking = bgg_games.loc[bgg_id]["AvgRating"]
            game.gameweight = bgg_games.loc[bgg_id]["GameWeight"]
            game.ranking = int(bgg_games.loc[bgg_id]["Rank:boardgame"])
        except IndexError:
            print(f"Couldn't find {game.name} in BGG database")


alphabetical_index = "https://www.pagat.com/alpha/"
pagat_base_url = "https://www.pagat.com"
r = httpx.get(alphabetical_index)
soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")

games: list[Game] = []
aliases: dict[str, str] = {}

# Iterate through rows
for row in table.find_all("tr"):
    # Ignore if row has less than 4 cells, this filters out rows like for "A"
    if len(row.find_all("td")) != 4:
        continue
    cells = row.find_all("td")
    name = cells[0].text.replace("\n", " ").strip()
    if " see " in name:
        aliases[name.split(" see ")[0]] = name.split(" see ")[1]
        continue

    url = cells[0].find("a").get("href").replace("../", "/")
    players = cells[1].text
    # Get the contained span title of the design cell
    try:
        design = cells[2].find("span").get("title")
    except AttributeError:
        design = cells[2].text
    quantity = cells[3].text
    game = Game(name, url, players, design, quantity)

    games.append(game)

# Add aliases to games
for alias, name in aliases.items():
    for game in games:
        if game.name == name:
            game.aliases.append(alias)
if GET_RULES:
    for game in games:
        game.rules = scrape_game_page(pagat_base_url + game.url)
        break

add_bgg_rankings(games)
# Export to JSON
import json

with open("games.json", "w", encoding="utf-8") as f:
    json.dump(games, f, indent=4, default=lambda o: o.__dict__, ensure_ascii=False)
