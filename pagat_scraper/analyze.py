import pandas as pd

# load games.json
games = pd.read_json("games.json")
print(games)

# Sort games by bgg_ranking
games = games.sort_values(by="bgg_ranking", ascending=False)
print(games)

# Print all games that have a BGG ranking to csv
games[games["bgg_ranking"].notnull()].to_csv("games_with_bgg_ranking.csv")
# Add url to name
games["name"] = games["name"].apply(lambda x: f"[{x}](https://www.pagat.com{games.loc[games['name'] == x]['url'].values[0]})")

# Drop url, aliases, and rules
games = games.drop(columns=["url", "aliases", "rules"])
# Now export it to a markdown table
games[games["bgg_ranking"].notnull()].to_markdown("games_with_bgg_ranking.md", index=False)

