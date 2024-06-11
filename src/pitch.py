

class Pitch:

    def __init__(self, pitch_x: float, pitch_y: float, pitch_type: str):

        self.pitch_x:float = pitch_x
        self.pitch_y:float = pitch_y
        self.pitch_type:str = pitch_type
        self.hitability:float= 0.0
        self.outcome:str = ""