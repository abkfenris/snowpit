from datetime import datetime
from lxml import etree

import arrow

from .layer import Layer
from .snowpit import Snowpit




def layer_from_element(element, ns):
    depth_element = element.find(ns + 'depthTop')
    depth = float(depth_element.text)
    return depth


def loads(xml):
    root = etree.fromstring(xml)
    ns = '{' + etree.QName(root.tag).namespace + '}'

    time_element = root.find(ns + 'validTime')
    time_instant = arrow.get(time_element.find(ns + 'TimeInstant').find(ns + 'timePosition').text).datetime

    position_element = root.find(ns + 'locRef')
    position_obs = position_element.find(ns + 'ObsPoint')
    position_point = position_obs.find(ns + 'pointLocation').find('{http://www.opengis.net/gml}Point').find('{http://www.opengis.net/gml}pos')
    lat, lon = position_point.text.split()

    pit = Snowpit(datetime=time_instant, latitude=lat, longitude=lon)

    profile = root.find(ns + 'snowProfileResultsOf').find(ns + 'SnowProfileMeasurements')
    strat = profile.find(ns + 'stratProfile')
    layers = strat.getchildren()

    return pit


def load(filename):
    with open(filename, 'rb') as f:
        return loads(f.read())
