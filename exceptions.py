"""
A module for custom exceptions
"""


class InvalidClockPeriod(ValueError):
    """
    Raised when invalid value of clock frequency is provided
    """
    pass


class OutputSignalOverflow(ValueError):
    """
    Raised when bit width of signal is too small (overflow happened)
    """
    pass
