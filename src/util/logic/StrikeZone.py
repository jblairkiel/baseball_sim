import math
from typing import List


class StrikeZone:

    def __init__(self):

        
        self.x0_full_bounds = -2.0
        self.x1_full_bounds = 2.0
        self.y0_full_bounds = -2.0
        self.y1_full_bounds = 2.0

        self.x0_strike_bounds = -1.0
        self.x1_strike_bounds = 1.0
        self.y0_strike_bounds = -1.0
        self.y1_strike_bounds = 1.0


    def get_full_bounds(self) -> List[List[float]]:

        return [
            [
                self.x0_full_bounds,
                self.x1_full_bounds
            ],
            [
                self.y0_full_bounds,
                self.y1_full_bounds
            ]
        ]
    
    
    def get_strike_bounds(self) -> List[List[float]]:

        return [
            [
                self.x0_strike_bounds,
                self.x1_strike_bounds
            ],
            [
                self.y0_strike_bounds,
                self.y1_strike_bounds
            ]
        ]
    def calculate_hitability(self) -> float:

        max_range = 4
        min_range = 0.1

        flat_odds_calculator = 0.1

