from src.player import Player
from src.team import Team


class League:

    def __init__(self, name, teams=[]):
        self.name = None
        self.teams = teams
        self.standings = []
