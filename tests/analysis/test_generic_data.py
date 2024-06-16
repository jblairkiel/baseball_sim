"""Module for Test Player"""

import pandas as pd
import plotly.graph_objects as go

from src.analysis.generic_data import Generic_Data
from src.util.randoms import generate_random_df


class TestGenericData:
    """Class for Player"""

    def test_Generic_Data(self):
        rand_df = generate_random_df()
        generic_data_obj = Generic_Data(rand_df)
        assert isinstance(generic_data_obj, Generic_Data)
        assert isinstance(generic_data_obj.df, pd.DataFrame)
        assert (
            isinstance(generic_data_obj.data_options, dict)
            or generic_data_obj.data_options is None
        )

    def test_histogram(self):
        rand_df = generate_random_df()
        generic_data_obj = Generic_Data(rand_df)
        hist = generic_data_obj.get_histogram("sepal_width")
        assert isinstance(hist, go.Figure)

    def test_pie(self):
        rand_df = generate_random_df()
        generic_data_obj = Generic_Data(rand_df)
        hist = generic_data_obj.get_pie("sepal_width")
        assert isinstance(hist, go.Figure)

    def test_scatter(self):
        rand_df = generate_random_df()
        generic_data_obj = Generic_Data(rand_df)
        hist = generic_data_obj.get_scatter(
            "sepal_width", "sepal_length", "test", "species"
        )
        assert isinstance(hist, go.Figure)
