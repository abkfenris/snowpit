class Layer(object):
    """
    A single layer in a Snowpit
    """
    def __init__(self, thickness, depth=None, hardness=None):
        """
        Create a new layer
        """
        self.thickness = thickness
        self.depth = depth
        self.hardness = hardness
