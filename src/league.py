from typing import List
from src.team import Team


class League:

    def __init__(self, name: str, teams: List[Team]=[]):
        self.name = None
        self.teams = teams
        self.standings = []
