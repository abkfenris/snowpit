class BasicTest(object):
    """
    Basic snow test
    """
    def __init__(self):
        self.results = None

    def results(self):
        return self.results

    def __str__(self):
        return '{0} - {1}'.format(type(self).__name__, self.results)

    def __repr__(self):
        return '< {0} - {1} >'.format(type(self).__name__, self.results)


class ShovelShearTest(BasicTest):
    """
    Column shear test performed with a shovel
    """
    def __init__(self):
        self.results = 'Dangerous'


class RutschblockTest(BasicTest):
    """
    """
    pass
