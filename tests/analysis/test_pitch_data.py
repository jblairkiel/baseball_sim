"""Module for Test Player"""

import plotly.express as px

from src.analysis.pitch_data import Pitch_Data


class TestPitchData:
    """Class for Player"""

    def test_Pitch_Data(self):
        # rand_df = generate_random_pitch_df()
        rand_df = px.data.iris
        pitch_data_obj = Pitch_Data(rand_df)
        assert isinstance(pitch_data_obj, Pitch_Data)
        assert isinstance(pitch_data_obj.options, list)
