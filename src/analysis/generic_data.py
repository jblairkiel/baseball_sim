import plotly.express as px

class Generic_Data:


    def __init__(self, df, data_options):

        self.df = df
        self.data_options = data_options

        #TODO Check if data_options are valid with df

    def get_histogram(self, data_item) -> px.histogram:

        his = px.histogram(
            self.df[data_item], 
            title=f"Histogram of {data_item}"
        )

        return his
    
    def show_histogram(self, data_item):

        his = self.get_histogram(data_item)
        his.show()

    def get_scatter(self, x, y, title, color) -> px.scatter:
        if color == None:
            loc = px.scatter(self.df, x=x, y=y,title=title)
        else:
            loc = px.scatter(self.df, x=x, y=y,title=title, color=color)

        loc.show()

    def show_scatter(self, x, y, title, color=None):

        scatt = self.get_scatter(x, y, title, color=color)
    
        scatt.show()