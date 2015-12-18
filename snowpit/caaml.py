"""Loading methods for CAAML XML http://caaml.org
"""
from lxml import etree

import arrow

from .layer import Layer
from .snowpit import Snowpit
import snowpit.test as test


def layer_from_element(element, ns):
    """
    Returns a new layer from an xml element
    """
    depth_element = element.find(ns + 'depthTop')
    depth = float(depth_element.text)

    thickness_element = element.find(ns + 'thickness')
    thickness = float(thickness_element.text)

    hardness_element = element.find(ns + 'hardness')
    hardness = hardness_element.text

    grain_element = element.find(ns + 'grainFormPrimary')
    grain = grain_element.text or None

    return Layer(thickness, depth=depth, hardness=hardness, grain_form=grain)


def test_from_element(element, ns):
    """
    returns a new test from an xml element
    """
    failed_element = element.find(ns + 'failedOn')
    depth = float(failed_element.find(ns + 'Layer').find(ns + 'depthTop').text)

    results_element = failed_element.find(ns + 'Results')
    score = results_element.find(ns + 'testScore').text
    print(depth, score)


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

    position_elevation_element = (position_obs.find(ns + 'validElevation')
                                  .find(ns + 'ElevationPosition'))
    elevation_unit = position_elevation_element.get('uom')
    elevation = float(position_elevation_element.find(ns + 'position').text)

    try:
        aspect = (position_obs.find(ns + 'validAspect')
                  .find(ns + 'AspectPosition')
                  .find(ns + 'position').text)
    except AttributeError:
        aspect = None

    profile = (root.find(ns + 'snowProfileResultsOf')
               .find(ns + 'SnowProfileMeasurements'))
    strat = profile.find(ns + 'stratProfile')
    layers = [layer_from_element(layer, ns) for layer in strat.getchildren()]

    temp_element = profile.find(ns + 'tempProfile')
    temps = []
    for temp in temp_element.getchildren():
        temps.append({'depth': temp.find(ns + 'depth').text,
                     'temp': temp.find(ns + 'snowTemp').text})
    temps.sort(key=lambda reading: reading['depth'])

    test_element = profile.find(ns + 'stbTests')
    for test in test_element.getchildren():
        print(test)
        test_from_element(test, ns)

    pit = Snowpit(datetime=time_instant,
                  latitude=lat,
                  longitude=lon,
                  layers=layers,
                  elevation=elevation,
                  elevation_unit=elevation_unit,
                  aspect=aspect,
                  temps=temps)
    return pit


def load(filename):
    """
    Return a Snowpit Object from XML file
    """
    with open(filename, 'rb') as f:
        return loads(f.read())
