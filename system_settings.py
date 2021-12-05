class SystemSettings:

    def __init__(self, desired_clk_freq: float = 0.5e9, bit_width: int = 16, desired_wave_freq: float = 1/350e-9):
        """
        Parameters needed for initialization of the system
        Args:
            desired_clk_freq: clock frequency of system
            bit_width: bit width of output signal
            desired_wave_freq: what frequency of square wave do we want to get
        """

        self.desired_clk_freq = desired_clk_freq
        self.bit_width = bit_width
        self.desired_wave_freq = desired_wave_freq

    @property
    def phase_limit(self) -> int:
        """
        Max counting value (int)
        """
        return int(self.desired_clk_freq / self.desired_wave_freq)

    @property
    def check_overflow(self) -> bool:
        """
        Indicator if an overflow happens. If it happens, bit width of the signal is not enough to generate signal
        properly
        """
        return True if self.desired_clk_freq / self.desired_wave_freq > 2 ** self.bit_width else False
