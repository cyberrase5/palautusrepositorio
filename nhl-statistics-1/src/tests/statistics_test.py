import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_top(self):
        self.assertEqual(self.statistics.top(4)[0].name, "Gretzky")

    def test_search_found(self):
        self.assertEqual(self.statistics.search("Semenko").team, "EDM")

    def test_search_not_found(self):
        self.assertEqual(self.statistics.search("Anttila"), None)

    def test_team(self):
        self.assertEqual(self.statistics.team("EDM")[0].name, "Semenko")