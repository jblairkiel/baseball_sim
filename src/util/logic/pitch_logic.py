import math
from random import gauss

from src.util.logic.StrikeZone import StrikeZone


class PitchLogic:

    def __init__(self, pitch_x, pitch_y, pitch_type):

        self.pitch_x = pitch_x
        self.pitch_y = pitch_y
        self.pitch_type = pitch_type

    def calculate_hitability(self, flat_odds_calculator=.1) -> float:

        full_pitch_bounds = StrikeZone().get_full_bounds()
        max_range = full_pitch_bounds[0][0] * 2
        min_range = 0.1

        rand_x_pitch = gauss(0, flat_odds_calculator)
        rand_y_pitch = gauss(0, flat_odds_calculator)
    
        # Closest to the sweet spot
        abs_x_hit_val = abs(self.pitch_x)
        x_hitability = (flat_odds_calculator / (abs_x_hit_val + 0.01)) - abs_x_hit_val

        abs_y_hit_val = abs(self.pitch_y)
        y_hitability = (flat_odds_calculator / (abs_y_hit_val + 0.01)) - abs_y_hit_val

        avg_hit = (x_hitability * y_hitability) / 2

        # Normalize
        norm_avg_hit = (avg_hit - min_range) / (max_range - min_range)
        return norm_avg_hit

    def calculate_radius_hitability(self) -> float:

        max_range = 4
        min_range = 0.1
        pi = math.pi

        max_radius = min_range * max_range

        radius = self.pitch_x * self.pitch_y
        radius_sq = radius * radius
        radius_hitability = 1 / (pi * radius_sq)

        normalized_radius = (radius_hitability - 0) / (1 - 0)
        return normalized_radius
