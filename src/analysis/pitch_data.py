import plotly.express as px
from src.analysis.generic_data import Generic_Data


class Pitch_Data(Generic_Data):

    def __init__(self, df):

        self.options = [{"col": "outcome", "title": "Call"}]
        super().__init__(df, self.options)

    def get_y_location_hist(self) -> px.scatter:

        his = self.get_histogram("y")
        return his

    def show_y_location_hist(self):

        his = self.get_y_location_hist()

        his.show()

    def get_x_location_hist(self) -> px.scatter:

        his = self.get_histogram("x")
        return his

    def show_x_location_hist(self):

        his = self.get_x_location_hist()

        his.show()
