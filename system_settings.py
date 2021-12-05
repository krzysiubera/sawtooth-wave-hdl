class SystemSettings:

    def __init__(self, desired_clk_freq=0.5e9, bit_width=16, desired_wave_freq=1/350e-9):
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
    def phase_limit(self):
        return int(self.desired_clk_freq / self.desired_wave_freq)
