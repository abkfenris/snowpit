"""
Snowpack tests

The snowpack tests are largely as defined in SWAG. Snow, Weather,
and Avalanches: Observational Guidelines for Avalanche Programs in the
United States which is available online at
http://www.americanavalancheassociation.org/swag/
"""


class BasicTest(object):
    """
    Basic snow test
    """
    def __init__(self, depth):
        self.results = None
        self.depth = depth

    def results(self):
        return self.results

    def __str__(self):
        return '{0} - {1}'.format(type(self).__name__, self.results)

    def __repr__(self):
        return '< {0} - {1} >'.format(type(self).__name__, self.results)


compression_scores = {
    'Very Easy': {
        'description': 'Fractures during cutting',
        'code': 'CTV'
    },
    'Easy': {
        'description': 'Fractures within 10 light taps using finger tips only',
        'code': 'CT1 - CT10'
    },
    'Moderate': {
        'description': ('Fractures within 10 moderate taps from the elbow '
                        'using finger tips'),
        'code': 'CT11 - CT20'
    },
    'Hard': {
        'description': ('Fractures within 10 firm taps from the whole arm '
                        'using palm or fist'),
        'code': 'CT21 - CT30'
    },
    'No Fracture': {
        'description': 'Does not fracture',
        'code': 'CTN'
    }
}


class CompressionTest(BasicTest):
    """
    Standard Compression Test as defined in section 2.7.4 of SWAG

    Arguments:
        - depth - Depth that the failure occured at
        - code - Data Code in the form of CT#
    """
    def __init__(self, depth, code):
        self.depth = depth
        self.results = code

    @property
    def score(self):
        end = self.results[2:].upper()
        if end == 'V':
            return 'Very Easy'
        if end == 'N':
            return 'No Fracture'
        if int(end) <= 10:
            return 'Easy'
        if int(end) <= 20:
            return 'Moderate'
        if int(end) <= 30:
            return 'Hard'

    @property
    def description(self):
        return compression_scores.get(self.score)['description']


class DeepTapTest(BasicTest):
    """
    Deep Tap Test as defined in section 2.7.5 of SWAG
    """
    pass


class ShovelShearTest(BasicTest):
    """
    Shovel Shear Test as defined in section 2.7.2 of SWAG
    """
    pass


class RutschblockTest(BasicTest):
    """
    Rutschblock Test as defined in section 2.7.3 of SWAG
    """
    pass


class StuffblockTest(BasicTest):
    """
    Stuffblock Test as defined in section 2.7.6 of SWAG
    """
    pass


extended_column_codes = {
    'ECTPV': 'Fracture propogates across the entire column during isolation ',
    'ECTP##': ('Fracture initiates and propogates across the entire column on '
               'the {num} tap and propogates across the column on the {num} '
               '+ 1 tap'),
    'ECTN##': ('Fracture initiates on the {num} tap, but does not propogate '
               'across the entire column on either {num} or the {num}+1 tap. '
               'It either fractures across only part of the column '
               '(observed commonly), or it initiates but takes more than one '
               'additional loading step to propogate across the entire column '
               '(observed relatively rarely).'),
    'ECTX': 'No fracture occurs during the test'
}


class ExtendedColumnTest(BasicTest):
    """
    Extended Column Test as defined in section 2.7.7 of SWAG
    """
    def __init__(self, depth, code):
        self.depth = depth
        self.results = code

    @property
    def num(self):
        return int(self.results[4:])

    @property
    def base_code(self):
        code = self.results.upper()
        if code == 'ECTPV':
            return 'ECTPV'
        if code == 'ECTX':
            return 'ECTX'
        if code[:4] == 'ECTP':
            return 'ECTP##'
        if code[:4] == 'ECTN':
            return 'ECTN##'

    @property
    def description(self):
        return extended_column_codes[self.base_code].format(num=self.num)



class PropogationSawTest(BasicTest):
    """
    Propogation Saw Test as defined in section 2.7.8 of SWAG
    """
    pass
