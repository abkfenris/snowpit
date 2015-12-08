import json

import arrow
from shapely.geometry import Point, asShape, mapping


class Snowpit(object):
    """
    Snowpit object
    """
    def __init__(self,
                 layers=None,
                 weather=None,
                 tests=None,
                 observations=None,
                 datetime=None,
                 time=None,
                 date=None,
                 point=None,
                 latitude=None,
                 longitude=None):
        """
        Initialize a new snowpit
        """
        if layers is None:
            layers = []
        if weather is None:
            weather = []
        if tests is None:
            tests = []
        if observations is None:
            observations = []
        self.layers = layers
        self.weather = weather
        self.tests = tests
        self.observations = observations

        if datetime is not None:
            self.datetime = datetime
        elif date is not None and time is not None:
            self.datetime = date + ' ' + time

        if point is not None:
            if type(point) == Point:
                self.point = point
            else:
                self.point = asShape(point)
        elif latitude is not None and longitude is not None:
            self.point = Point(float(longitude), float(latitude))
        else:
            self.point = None

    @property
    def datetime(self):
        """
        Returns a datetime object for the Snowpit
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetimestring):
        """
        Set time from a string that arrow can understand
        """
        self._datetime = arrow.get(datetimestring).datetime

    @property
    def datetime_str(self):
        """
        Returns a formatted datetime string
        """
        return self.datetime.strftime('%Y-%m-%d %H:%M')

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

    def add_layer(self, layer):
        """
        Adds a layer to the snowpit's existing layers
        """
        if layer not in self.layers:
            self.layers.append(layer)
            self.layers.sort(key=lambda x: x.depth)

    @property
    def lat(self):
        """
        Returns latitude
        """
        return self.point.y

    @property
    def lon(self):
        """
        Returns longitude
        """
        return self.point.x

    @property
    def geojson(self):
        """
        Returns geojson/python geo interface for Snowpit
        """
        return mapping(self.point)

    @property
    def geojson_feature(self):
        """
        Returns a geojson feature for Snowpit
        """
        return json.dumps({
            'type': 'Feature',
            'geometry': self.geojson,
            'properties': {
                'datetime': str(self.datetime),
            }
        })

    def __repr__(self):
        """
        Human readable representation of snowpit
        """
        if self.datetime is not None and self.point is not None:
            return '<Snowpit {datetime} - {lat}, {lon}>'.format(datetime=self.datetime_str,
                                                                lat=self.lat,
                                                                lon=self.lon)
        elif self.datetime is not None:
            return '<Snowpit {datetime}>'.format(datetime=self.datetime_str)
        elif self.point is not None:
            return '<Snowpit {lat}, {lon}>'.format(lat=self.lat,
                                                   lon=self.lon)
