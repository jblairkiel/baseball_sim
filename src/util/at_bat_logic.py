
from src import pitch, player
from src.util.logic.pitcher_hitter_logic import PitcherHitterLogic


def get_pitch_at_atbat(player: player, pitch: pitch):
    ph_obj = PitcherHitterLogic(player.get_slugging_percentage())
    pitch.hitability = ph_obj.calculate_hitability_value(pitch.pitch_x, pitch.pitch_y, hit_odds_calculator=.20)
    pitch.outcome = ph_obj.get_ump_call_outcome(pitch.pitch_x, pitch.pitch_y)
    pitch.outcome = ph_obj.determine_hitability_from_value(pitch.pitch_x, pitch.pitch_y, pitch.hitability, pitch.outcome)
    return pitch.outcome