import math
from random import gauss

import numpy as np
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

        rand_x_pitch = pitch.pitch_x
        rand_y_pitch = pitch.pitch_y
        mean = 0
        sig = 1
        
        gaussian_value = np.exp(-((rand_x_pitch - mean)**2 + (rand_y_pitch - mean)**2) / (2 * sig**2))

        return gaussian_value

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
