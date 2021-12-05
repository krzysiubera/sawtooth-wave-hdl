import unittest
from system_settings import SystemSettings
from sawtooth_signal_tb import sawtooth_tb
import sawtooth_signal_tb


class TestSawtoothSignalGenerator(unittest.TestCase):
    """
    A class for testing of the block generating sawtooth signal
    """

    def test_periods_signal(self):
        """
        Simple test case with clock frequency 0.5 MHz, 16 bit width, desired period of signal 350 ns.
        Generating from 1 to 7 periods of the signal
        """
        self.system_settings = SystemSettings()

        for period_to_run in range(1, 8):
            self.periods_to_run = period_to_run
            tb = sawtooth_tb(self.system_settings, periods=self.periods_to_run)
            tb.run_sim()

            expected_wave = self.get_expected_wave()
            self.assertEqual(sawtooth_signal_tb.results, expected_wave)
            sawtooth_signal_tb.results = []

    def test_signal_frequency(self):
        """
        Testing frequency of the generated signal. Frequency 200 MHz, 16 bit width, frequency of the generated wave
        varies. Generating 8 periods of the signal
        """
        for signal_freq in (1000, 2000, 3000, 4000, 5000):
            self.periods_to_run = 8
            self.system_settings = SystemSettings(desired_clk_freq=2e6, bit_width=16, desired_wave_freq=signal_freq)
            tb = sawtooth_tb(self.system_settings, periods=self.periods_to_run)
            tb.run_sim()

            expected_wave = self.get_expected_wave()
            self.assertEqual(sawtooth_signal_tb.results, expected_wave)
            sawtooth_signal_tb.results = []

    def test_invalid_clock_value(self):
        """
        Value of half of clock period (scaled to nano seconds) should be an integer not equal to 0. If this is the
        case, then exception ValueError should be thrown
        """
        with self.assertRaises(ValueError, msg="Invalid value of clock frequency provided"):
            self.periods_to_run = 2
            self.system_settings = SystemSettings(desired_clk_freq=1e9, bit_width=16, desired_wave_freq=1 / 350e-9)
            tb = sawtooth_tb(self.system_settings, periods=self.periods_to_run)
            tb.run_sim()

    def get_expected_wave(self):
        return [num % self.system_settings.phase_limit for num in range(0, self.periods_to_run *
                                                                        self.system_settings.phase_limit)]


if __name__ == '__main__':
    unittest.main(verbosity=2)

