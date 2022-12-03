class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score_player1_zero_points(self):
        difference = self.m_score1 - self.m_score2

        if difference == 0: # 0 - 0
            return "Love-All"
        elif difference == -1: # 0 - 1 
            return "Love-Fifteen"
        elif difference == -2: # 0 - 2
            return "Love-Thirty"
        elif difference == -3: # 0 - 3
            return "Love-Forty"
        elif difference == -4: # 0 - 4
            return "Win for player2"

    def get_score_player1_one_points(self):
        difference = self.m_score1 - self.m_score2

        if difference == 1: # 1 - 0
            return "Fifteen-Love"
        elif difference == 0: # 1 - 1 
            return "Fifteen-All"
        elif difference == -1: # 1 - 2
            return "Fifteen-Thirty"
        elif difference == -2: # 1 - 3
            return "Fifteen-Forty"
        elif difference == -3: # 1 - 4
            return "Win for player2"

    def get_score_player1_two_points(self):
        difference = self.m_score1 - self.m_score2

        if difference == 2: # 2 - 0
            return "Thirty-Love"
        elif difference == 1: # 2 - 1 
            return "Thirty-Fifteen"
        elif difference == 0: # 2 - 2
            return "Thirty-All"
        elif difference == -1: # 2 - 3
            return "Thirty-Forty"
        elif difference == -2: # 2 - 4
            return "Win for player2"

    def get_score_player1_three_points(self):
        difference = self.m_score1 - self.m_score2

        if difference == 3: # 3 - 0
            return "Forty-Love"
        elif difference == 2: # 3 - 1 
            return "Forty-Fifteen"
        elif difference == 1: # 3 - 2
            return "Forty-Thirty"
        elif difference == 0: # 3 - 3
            return "Forty-All"
        elif difference == -1: # 3 - 4
            return "Advantage player2"

        return ""

    def get_score_player1_four_points(self):
        difference = self.m_score1 - self.m_score2

        if difference == 4: # 4 - 0
            return "Win for player1"
        elif difference == 3: # 4 - 1 
            return "Win for player1"
        elif difference == 2: # 4 - 2
            return "Win for player1"
        elif difference == 1: # 4 - 3
            return "Advantage player1"
        elif difference == 0: # 4 - 4
            return "Deuce"

        return ""

    def get_score_other(self):
        difference = self.m_score1 - self.m_score2

        if self.m_score1 > self.m_score2: # p1 winning
            if difference >= 2: # by how much
                return "Win for player1"
            else:
                return "Advantage player1"

        
        if self.m_score1 < self.m_score2: # p2 winning
            if difference <= -2: # by how much
                return "Win for player2"
            else:
                return "Advantage player2"


    def get_score(self):
        score = ""

        if self.m_score1 == 0:
            score = self.get_score_player1_zero_points()
        elif self.m_score1 == 1:
            score = self.get_score_player1_one_points()
        elif self.m_score1 == 2:
            score = self.get_score_player1_two_points()
        elif self.m_score1 == 3:
            score = self.get_score_player1_three_points()
        elif self.m_score1 == 4:
            score = self.get_score_player1_four_points()

        if score == "":
            score = self.get_score_other()

        return score
