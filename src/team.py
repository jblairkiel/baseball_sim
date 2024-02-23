from src.player import Player

class Team():

    def __init__(self, name, players=[], coach=None, teamValue=None):
        self.name = name
        self.players = players
        self.coach = coach
        self.wins = 0
        self.losses = 0
        self.team_value = 0

    def __str__(self):
        newline = '\n'
        newlinenewtab = '\n\t'
        roster_str =  f"Lineup: {newlinenewtab} {newlinenewtab.join(map(str, self.players))}"
        return f"{self.name} ({self.wins}-{self.losses}) {newline} {roster_str}"

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def get_batting_average(self):
        total_batting_average = 0
        total_at_bats = 0
        for player in self.players:
            total_batting_average += player.get_batting_average() * player.stats['at_bats']
            total_at_bats += player.stats['at_bats']
        return total_batting_average / total_at_bats if total_at_bats > 0 else 0

    def get_on_base_percentage(self):
        total_on_base_percentage = 0
        total_at_bats = 0
        for player in self.players:
            total_on_base_percentage += player.get_on_base_percentage() * player.stats['at_bats']
            total_at_bats += player.stats['at_bats']
        return total_on_base_percentage / total_at_bats if total_at_bats > 0 else 0

    def get_slugging_percentage(self):
        total_slugging_percentage = 0
        total_at_bats = 0
        for player in self.players:
            total_slugging_percentage += player.get_slugging_percentage() * player.stats['at_bats']
            total_at_bats += player.stats['at_bats']
        return total_slugging_percentage / total_at_bats if total_at_bats > 0 else 0

    def record_win(self):
        self.wins += 1

    def record_loss(self):
        self.losses += 1