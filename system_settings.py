from dataclasses import dataclass


@dataclass
class SystemSettings:
    clk_freq: float = 0.5e9     # clock frequency of the system
    bit_width: int = 16         # bit width of the output signal
    wave_freq: float = 1e6      # frequency of output sawtooth signal

    @property
    def phase_limit(self) -> int:
        """
        Max counting value (int)
        """
        return int(self.clk_freq / self.wave_freq)

    @property
    def check_overflow(self) -> bool:
        """
        Indicator if an overflow happens. If it happens, bit width of the signal is not enough to generate signal
        properly
        """
        return self.clk_freq / self.wave_freq > 2 ** self.bit_width
