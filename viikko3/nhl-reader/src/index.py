from playerReader import playerReader
from playerStats import playerStats

def main():
    
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = playerReader(url)
    stats = playerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
