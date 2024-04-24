"""Module for Test Team"""

from src.util.generation import generate_pitch


class TestPitch:
    """Class for Team"""

    # def test_single_team_generate():
    #     x = generate_team()
    #     assert type(x) == Team

    def test_generate_pitch_is_not_none(self):
        """Tests if Nones are passed in"""
        pitch = generate_pitch()
        assert pitch is not None

    def test_pitch_attrs_are_not_none(self):
        pitch = generate_pitch()
        assert pitch.pitch_x is not None
        assert pitch.pitch_y is not None
        assert pitch.pitch_type is not None
        assert pitch.hitability is not None
        assert pitch.outcome is not None