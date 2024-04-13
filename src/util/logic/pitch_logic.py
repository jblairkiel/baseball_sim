import math
from random import gauss
from src.pitch import Pitch

from src.util.logic.StrikeZone import StrikeZone


class PitchLogic:

    def __init__(self):

        strike_pitch_bounds = StrikeZone().get_strike_bounds()
        self.x0_strike_bounds  = strike_pitch_bounds[0][0]
        self.x1_strike_bounds = strike_pitch_bounds[0][1]
        self.y0_strike_bounds = strike_pitch_bounds[1][0]
        self.y1_strike_bounds = strike_pitch_bounds[1][1]
        
    def get_outcome(self, pitch: Pitch)->Pitch:
        # Implement Ump Error
        if (self.x0_strike_bounds < pitch.pitch_x < self.x1_strike_bounds) and (
            self.y0_strike_bounds < pitch.pitch_y < self.y1_strike_bounds
        ):
            pitch.outcome = "Strike"
        else:
            pitch.outcome = "Ball"

        return pitch

    def calculate_hitability(self, pitch: Pitch, hit_odds_calculator=1.5) -> float:

        full_pitch_bounds = StrikeZone().get_full_bounds()
        strike_bounds = StrikeZone().get_strike_bounds()
        max_range = full_pitch_bounds[0][0] * 2
        strike_range = strike_bounds[0][0] * 2
        min_range = 0.1

        rand_x_pitch = gauss(0, max_range / hit_odds_calculator)
        rand_y_pitch = gauss(0, max_range / hit_odds_calculator)
    
        # Closest to the sweet spot
        x_hitability = abs(pitch.pitch_x) - strike_range
        #x_hitability = (flat_odds_calculator / (abs_x_hit_val + 0.01)) - abs_x_hit_val
        x_hitability = (rand_x_pitch / strike_range) - strike_range

        abs_y_hit_val = abs(pitch.pitch_y)
        #y_hitability = (flat_odds_calculator / (abs_y_hit_val + 0.01)) - abs_y_hit_val
        y_hitability = (rand_y_pitch / strike_range) - strike_range

        avg_hit = (x_hitability * y_hitability) / 2

        # Normalize
        norm_avg_hit = (avg_hit - min_range) / (max_range - min_range)
        return norm_avg_hit

    def calculate_radius_hitability(self, pitch: Pitch) -> float:

        max_range = 4
        min_range = 0.1
        pi = math.pi

        max_radius = min_range * max_range

        radius = pitch.pitch_x * pitch.pitch_y
        radius_sq = radius * radius
        radius_hitability = 1 / (pi * radius_sq)

        normalized_radius = (radius_hitability - 0) / (1 - 0)
        return normalized_radius
