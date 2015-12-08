class Layer(object):
    """
    A single layer in a Snowpit
    """
    def __init__(self, thickness, depth=None, hardness=None, grain_form=None):
        """
        Create a new layer
        """
        self.thickness = float(thickness)
        self.depth = float(depth)
        self.hardness = str(hardness)
        self.grain_form = str(grain_form)

    def __repr__(self):
        output = '<Layer'
        if self.thickness:
            output += ' - Thickness: ' + str(self.thickness)
        if self.depth is not None:
            output += ' - Depth: ' + str(self.depth)
        if self.hardness:
            output += ' - Hardness: ' + self.hardness
        if self.grain_form:
            output += ' - Grain Form: ' + self.grain_form
        output += '>'
        return output
