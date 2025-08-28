class AnyWithin:
    """Matches any value within a numeric range and supports + and - arithmetic.

    For hacking test for window size only.
    """

    def __init__(self, low, high):
        self.low = low
        self.high = high

    # Equality check for testing
    def __eq__(self, other):
        try:
            return self.low <= other <= self.high
        except TypeError:
            return False

    # Addition
    def __add__(self, other):
        return other + self.high if isinstance(other, (int, float)) else NotImplemented

    def __radd__(self, other):
        return other + self.high if isinstance(other, (int, float)) else NotImplemented

    # Subtraction
    def __sub__(self, other):
        return self.low - other if isinstance(other, (int, float)) else NotImplemented

    def __rsub__(self, other):
        return other - self.high if isinstance(other, (int, float)) else NotImplemented

    def __repr__(self):
        return f"AnyWithin({self.low}, {self.high})"
