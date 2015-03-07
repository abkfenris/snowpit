import arrow

class Snowpit(object):
    """
    Snowpit object
    """
    def __init__(self, layers=[], weather=[], tests=[], observations=[], datetime=None, time=None, date=None):
        """
        Initialize a new snowpit
        """
        self.layers = layers
        self.weather = weather
        self.tests = tests
        self.observations = observations
        if datetime is not None:
            self.set_datetime(datetime)
        elif date is not None and time is not None:
            self.set_datetime(date + ' ' + time)

    def set_datetime(self, datetimestring):
        """
        Set time from a string that arrow can understand
        """
        self.datetime = arrow.get(datetimestring).datetime

    def get_datetime(self):
        """
        Returns a datetime object for the Snowpit
        """
        return self.datetime

    def get_datetime_str(self):
        """
        Returns a formatted datetime string
        """
        return self.datetime.strftime('%Y-%m-%d %H-%M')

    def get_date_str(self):
        """
        Returns a legible date for the snowpit
        """
        return self.datetime.date().strftime('%Y-%m-%d')

    def get_time_str(self):
        """
        Returns a string for time of snowpit
        """
        return self.datetime.time().strftime('%H-%M')

    def get_layers(self):
        """
        Returns a list of snowpit layers
        """
        return self.layers

    def add_layer(self, layer):
        """
        Adds a layer to the snowpit's existing layers
        """
        if layer not in self.layers:
            self.layers.append(layer)
            self.layers.sort(key=lambda x: x.depth)
