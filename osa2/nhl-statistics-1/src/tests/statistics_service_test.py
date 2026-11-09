import unittest
from  statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  # = 16
            Player("Lemieux", "PIT", 45, 54), # = 99
            Player("Kurri",   "EDM", 37, 53), # = 90
            Player("Yzerman", "DET", 42, 56), # = 98
            Player("Gretzky", "EDM", 35, 89)  # = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_print_top_scorers_success(self):
        top_players = self.stats.top(5)
        correct_order = []
        correct_order.append(self.stats.search("Gretzky"))
        correct_order.append(self.stats.search("Lemieux"))
        correct_order.append(self.stats.search("Yzerman"))
        correct_order.append(self.stats.search("Kurri"))
        correct_order.append(self.stats.search("Semenko"))

        self.assertEqual(top_players, correct_order)

    def test_searh_player_not_found(self):
        searched_player = self.stats.search("Sherwood")
        self.assertEqual(searched_player, None)

    def test_print_team_correctly(self):
        team = self.stats.team("PIT")
        correct_team = []
        correct_team.append(self.stats.search("Lemieux"))

        self.assertEqual(team, correct_team)

    def test_print_incorrect_team(self):
        team = self.stats.team("SJS")
        correct_team = []

        self.assertEqual(team, correct_team)
