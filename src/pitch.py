import math
from random import gauss

from src.util.logic.StrikeZone import StrikeZone


class Pitch:

    def __init__(self, pitch_x, pitch_y, pitch_type):

        self.pitch_x = pitch_x
        self.pitch_y = pitch_y
        self.pitch_type = pitch_type
