from random import gauss

import random as rand

import math
from random import gauss, random

import numpy as np
from src.pitch import Pitch

from src.util.logic.StrikeZone import StrikeZone

class PitcherHitterLogic:

    def __init__(self, slug_pct):
        
        self.rand_hit = .35
        self.ump_odds = .25
        self.hitability = (slug_pct) * self.rand_hit
        
        strike_pitch_bounds = StrikeZone().get_strike_bounds()
        self.x0_strike_bounds  = strike_pitch_bounds[0][0]
        self.x1_strike_bounds = strike_pitch_bounds[0][1]
        self.y0_strike_bounds = strike_pitch_bounds[1][0]
        self.y1_strike_bounds = strike_pitch_bounds[1][1]
        
    def get_swing_outcome(self, pitch_x: float, pitch_y: float, hitability: float)->str:
        
        rand_pitch_hitability = hitability
        cur_hitability = self.determine_hitability_from_value(pitch_x, pitch_y, rand_pitch_hitability)
    
        return cur_hitability

    def determine_hitability_from_value(self, pitch_x: float, pitch_y: float, pitch_hitability: float, ump_outcome:str, rand_pitch_hitability: float=.02) -> str:

        rand_chance = (pitch_hitability * rand.randrange(0, self.rand_hit * 100)) / 100
        if ump_outcome == "Strike":
            is_strike = True
        else: 
            is_strike = False
        if is_strike:
            if  pitch_hitability > (rand_pitch_hitability + rand_chance):
                outcome = "Hit"
            else :
                outcome = "Strike"
        else: 
            if  pitch_hitability < (rand_pitch_hitability + rand_chance):
                outcome = "Ball"
            else:
                outcome = "Strike"
        return outcome

        
    def get_ump_call_outcome(self, pitch_x: float, pitch_y: float)->str:
        # Implement Ump Error
        if (self.x0_strike_bounds < pitch_x < self.x1_strike_bounds) and (
            self.y0_strike_bounds < pitch_y < self.y1_strike_bounds
        ):
            outcome = "Strike"
        else:
            outcome = "Ball"

        return outcome

    def calculate_hitability_value(self, pitch_x: float, pitch_y: float, hit_odds_calculator=.45) -> float:

        full_pitch_bounds = StrikeZone().get_full_bounds()
        strike_bounds = StrikeZone().get_strike_bounds()

        rand_x_pitch = pitch_x
        rand_y_pitch = pitch_y
        mean = 0
        sig = 1
        
        gaussian_value = np.exp(-((rand_x_pitch - mean)**2 + (rand_y_pitch - mean)**2) / (2 * sig**2))
        #gaussian_value = gauss(0 ,sigma=)
        gaussian_value = gaussian_value * hit_odds_calculator
        return gaussian_value

    def calculate_radius_hitability(self, pitch_x: float, pitch_y: float) -> float:

        max_range = 4
        min_range = 0.1
        pi = math.pi

        max_radius = min_range * max_range

        radius = pitch_x * pitch_y
        radius_sq = radius * radius
        radius_hitability = 1 / (pi * radius_sq)

        normalized_radius = (radius_hitability - 0) / (1 - 0)
        return normalized_radius

    def is_strike(self, pitch_x: float, pitch_y: float, ump_odds=.12) -> bool:
        margin = (rand.randrange(0, ump_odds * 100)) / 100
        threshold = abs(self.x0_strike_bounds)

        x0_margin = self.x0_strike_bounds - margin
        x1_margin = self.x1_strike_bounds + margin
        y0_margin = self.y0_strike_bounds - margin
        y1_margin = self.y1_strike_bounds + margin
        
        # Check if the inputs fall within the expanded bounds
        if pitch_x < x0_margin or pitch_x > x1_margin or pitch_y < y0_margin or pitch_y > y1_margin:
            return False
        
        # Calculate the Gaussian curve value for the given inputs
        sigma = ump_odds + .3
        mean = 0   # Mean (center of the curve)
        gaussian_value = np.exp(-((pitch_x - mean)**2 + (pitch_y - mean)**2) / (2 * sigma**2))
        
        # Check if the Gaussian curve value is greater than the threshold
        return gaussian_value >= threshold

# Example usage: