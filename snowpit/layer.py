class Layer(object):
    """
    A single layer in a Snowpit
    """
    def __init__(self, thickness, depth=None, hardness=None):
        """
        Create a new layer
        """
        self.thickness = float(thickness)
        self.depth = float(depth)
        self.hardness = str(hardness)

    def get_thickness(self):
        """
        return the current layer thickness
        """
        return self.thickness

    def __repr__(self):
        return '<Layer - Thickness: {thickness} - Depth: {depth} - Hardness: {hardness}>'.format(thickness=self.thickness,
                                                                                          hardness=self.hardness,
                                                                                          depth=self.depth)
