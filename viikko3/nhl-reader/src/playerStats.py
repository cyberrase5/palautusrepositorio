class playerStats:

    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = sorted(self.players, reverse=True, key=points)
        ret = []

        for player in players:
            if (player.nationality == nationality):
                ret.append(player)

        return ret

def points(player):
        return player.goals + player.assists