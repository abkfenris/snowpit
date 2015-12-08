"""Loading methods for CAAML XML http://caaml.org
"""
from lxml import etree

import arrow

from .layer import Layer
from .snowpit import Snowpit


def layer_from_element(element, ns):
    depth_element = element.find(ns + 'depthTop')
    depth = float(depth_element.text)

    thickness_element = element.find(ns + 'thickness')
    thickness = float(thickness_element.text)

    hardness_element = element.find(ns + 'hardness')
    hardness = hardness_element.text

    grain_element = element.find(ns + 'grainFormPrimary')
    grain = grain_element.text or None

    return Layer(thickness, depth=depth, hardness=hardness, grain_form=grain)


def loads(xml):
    """
    Return a Snowpit object from XML String
    """
    root = etree.fromstring(xml)
    ns = '{' + etree.QName(root.tag).namespace + '}'

    time_element = root.find(ns + 'validTime')
    time_instant = (arrow.get(time_element.find(ns + 'TimeInstant')
                    .find(ns + 'timePosition').text).datetime)

    position_element = root.find(ns + 'locRef')
    position_obs = position_element.find(ns + 'ObsPoint')
    position_point = (position_obs.find(ns + 'pointLocation')
                      .find('{http://www.opengis.net/gml}Point')
                      .find('{http://www.opengis.net/gml}pos'))
    lat, lon = position_point.text.split()

    profile = (root.find(ns + 'snowProfileResultsOf')
               .find(ns + 'SnowProfileMeasurements'))
    strat = profile.find(ns + 'stratProfile')
    layers = [layer_from_element(layer, ns) for layer in strat.getchildren()]

    pit = Snowpit(datetime=time_instant,
                  latitude=lat,
                  longitude=lon,
                  layers=layers)
    return pit


def load(filename):
    """
    Return a Snowpit Object from XML file
    """
    with open(filename, 'rb') as f:
        return loads(f.read())
