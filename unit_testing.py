import unittest
from system_settings import SystemSettings
from sawtooth_signal_tb import sawtooth_tb
import sawtooth_signal_tb
from exceptions import OutputSignalOverflow, InvalidClockPeriod


class TestSawtoothSignalGenerator(unittest.TestCase):
    """
    A class for testing of the block generating sawtooth signal
    """

    def test_periods_signal(self):
        """
        Simple test case with clock frequency 0.5 MHz, 16 bit width, desired period of signal 350 ns.
        Generating from 1 to 7 periods of the signal and checking if output signal is the same as expected.
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
        Testing frequency of the generated signal. Clock frequency 200 MHz, 16 bit width, frequency of the generated
        wave is changing. Generating 8 periods of the signal and checking if output signal is the same as expected.
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
        case, then exception InvalidClockPeriod should be thrown
        """
        with self.assertRaises(InvalidClockPeriod):
            self.periods_to_run = 1
            self.system_settings = SystemSettings(desired_clk_freq=1e9, bit_width=16, desired_wave_freq=1 / 350e-9)
            tb = sawtooth_tb(self.system_settings, periods=self.periods_to_run)
            tb.run_sim()

    def test_overflow(self):
        """
        An overflow happens, when bit width is too small to handle desired clock and wave frequency. There is a property
        in SystemSettings class (check_overflow) which is an indicator if an overflow happened. This test checks if an
        exception is raised when check_overflow is True. If check_overflow is False, an exception should not happen.
        """

        # common settings for the test
        clk_freq = 0.5*1e9
        bit_width = 3
        self.periods_to_run = 1

        # frequency of desired wave frequency is changing
        for wave_freq in (0.5*1e4, 0.5*1e5, 0.5*1e6, 0.5*1e7, 0.5*1e8):
            self.system_settings = SystemSettings(desired_clk_freq=clk_freq, bit_width=bit_width,
                                                  desired_wave_freq=wave_freq)

            if self.system_settings.check_overflow:
                with self.assertRaises(OutputSignalOverflow):
                    tb = sawtooth_tb(system_settings=self.system_settings, periods=self.periods_to_run)
                    tb.run_sim()
            else:
                # testing if exception has not been thrown
                try:
                    tb = sawtooth_tb(system_settings=self.system_settings, periods=self.periods_to_run)
                    tb.run_sim()
                except OutputSignalOverflow:
                    self.fail("Test overflow failed")
                else:
                    self.assertTrue(1)

    def get_expected_wave(self):
        return [num % self.system_settings.phase_limit for num in range(0, self.periods_to_run *
                                                                        self.system_settings.phase_limit)]

    def tearDown(self) -> None:
        self.system_settings = None
        self.periods_to_run = None
        sawtooth_signal_tb.results = []


if __name__ == '__main__':
    unittest.main(verbosity=2)

