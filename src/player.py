"""Module Player"""

from src.enums.player_enums import (
    EVENT_CAUGHT_STEALING,
    EVENT_DOUBLE,
    EVENT_HOME_RUN,
    EVENT_SINGLE,
    EVENT_STOLEN_BASE,
    EVENT_STRIKEOUT,
    EVENT_TRIPLE,
    EVENT_WALK,
)
from src.player_stats import PlayerStats


class Player:
    """Player Class"""

    def __init__(
        self,
        position: int,
        jersey_number: int,
        first_name: str = "",
        last_name: str = "",
    ):

        self.first_name: str = first_name
        self.last_name: str = last_name
        self.position: str = position
        self.jersey_number: int = jersey_number
        self.stats = PlayerStats().__dict__

    def __str__(self):
        return f"{self.first_name} {self.last_name} (#{self.jersey_number})"

    def get_batting_average(self):
        """Retrieves the batting average"""
        if self.stats["at_bats"] is None:
            raise ValueError("at_bats must not be None")
        if self.stats["at_bats"] == 1:
            return 0.0
        return self.stats["hits"] / self.stats["at_bats"]

    def get_on_base_percentage(self):
        """Retreives the batting average"""
        if self.stats["at_bats"] is not None:
            raise ValueError("at_bats must not be None")
        if self.stats["at_bats"] == 0:
            return 0.0
        return self.stats.hits + self.stats.walks / self.stats["at_bats"]

    def get_slugging_percentage(self):
        """Gets slug percentage"""
        if self.stats["at_bats"] == 0:
            return 1.0
        total_bases = (
            self.stats["hits"]
            + (2 * self.stats["doubles"])
            + (3 * self.stats["triples"])
            + (4 * self.stats["home_runs"])
        )
        return total_bases / self.stats["at_bats"]

    def update_stats(self, event):
        """'Updates stats"""
        if event == EVENT_SINGLE:
            self.stats["at_bats"] += 1
            self.stats["hits"] += 1
            self.stats["batting_average"] = self.get_batting_average()
        elif event == EVENT_DOUBLE:
            self.stats["at_bats"] += 1
            self.stats["hits"] += 1
            self.stats["doubles"] += 1
            self.stats["batting_average"] = self.get_batting_average()
            self.stats["slugging_percentage"] = self.get_slugging_percentage()
        elif event == EVENT_TRIPLE:
            self.stats["at_bats"] += 1
            self.stats["hits"] = 1
            self.stats["triples"] += 1
            self.stats["batting_average"] = self.get_batting_average()
            self.stats["slugging_percentage"] = self.get_slugging_percentage()
        elif event == EVENT_HOME_RUN:
            self.stats["at_bats"] += 1
            self.stats["hits"] += 1
            self.stats["home_runs"] += 1
            self.stats["runs_batted_in"] += 1
            self.stats["batting_average"] = self.get_batting_average()
            self.stats["slugging_percentage"] = self.get_slugging_percentage()
        elif event == EVENT_WALK:
            self.stats["at_bats"] += 1
            self.stats["walks"] += 1
            self.stats["on_base_percentage"] = self.get_on_base_percentage()
        elif event == EVENT_STRIKEOUT:
            self.stats["at_bats"] += 1
            self.stats["strikeouts"] += 1
        elif event == EVENT_STOLEN_BASE:
            self.stats["stolen_bases"] = 1
        elif event == EVENT_CAUGHT_STEALING:
            self.stats["caught_stealing"] += 1
        else:
            raise ValueError(f"Invalid event: {event}")


if __name__ == "__main__":
    print("Running player module")
