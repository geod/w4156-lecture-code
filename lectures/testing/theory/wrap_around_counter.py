

class WrapAroundCounter:
    """Simple wrap around counter that increments
    an input wrapping around a max_value"""

    def __init__(self, max_val):
        self._max_val = max_val

    def increment(self, i: int):
        """
        :param i: integer between 0 and max_val
        :return: increments i wrapping around max_value
        """
        ret_val = None
        if i >= self._max_val or i < 1:
            ret_val = 1
        else:
            ret_val = i+1
        return ret_val
