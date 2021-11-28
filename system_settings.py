class SystemSettings:

    def __init__(self, target_freq=440, clk_freq=100000, bit_width=16):
        self.target_freq = target_freq
        self.clk_freq = clk_freq
        self.bit_width = bit_width

    @property
    def phase_limit(self):
        return (self.target_freq * (2 ** self.bit_width)) // self.clk_freq
