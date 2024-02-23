import math

class Pitch_Logic():


    def __init__(self, pitch_x, pitch_y, pitch_type):

        self.pitch_x = pitch_x
        self.pitch_y = pitch_y
        self.pitch_type = pitch_type

    def calculate_hitability(self) -> float:

        max_range = 4
        min_range = .1

        flat_odds_calculator = .1

        #Closest to the sweet spot
        abs_x_hit_val =  abs(self.pitch_x)
        x_hitability = (flat_odds_calculator / (abs_x_hit_val + .01)) - abs_x_hit_val 

        
        abs_y_hit_val =  abs(self.pitch_y)
        y_hitability = (flat_odds_calculator / (abs_y_hit_val + .01)) - abs_y_hit_val

        avg_hit = (x_hitability *  y_hitability) / 2

        #Normalize 
        norm_avg_hit = (avg_hit - min_range) / (max_range - min_range)
        return avg_hit

    def calculate_radius_hitability(self) -> float:

        
        max_range = 4
        min_range = .1
        pi = math.pi

        max_radius = max_radius * max_range

        radius = self.pitch_x * self.pitch_y
        radius_sq = radius * radius
        radius_hitability = 1 / (pi * radius_sq)

        normalized_radius = (radius_hitability - 0) / (1 - 0) 