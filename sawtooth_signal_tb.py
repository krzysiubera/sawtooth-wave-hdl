from myhdl import always, delay, StopSimulation, instance, Signal, intbv, block, ResetSignal
from sawtooth_signal import generate_sawtooth_signal
from system_settings import SystemSettings


results = []


@block
def sawtooth_tb(system_settings: SystemSettings, periods: int):
    """
    Test bench for sawtooth wave generator
    Args:
        system_settings: (SystemSettings) - settings for the system encapsulated in the class
        periods: (int) - how many periods of the signal do we want to create

    Yields:
        DUT: instance of the tested device
        drive_clk: process driving clock
        stimulus: process driving the application
    """

    # declare signals
    output = Signal(intbv(0)[system_settings.bit_width:])
    clk = Signal(bool(0))
    reset = ResetSignal(1, active=1, isasync=False)

    # instantiate DUT
    DUT = generate_sawtooth_signal(output=output, clk=clk, reset=reset, bit_width=system_settings.bit_width,
                                   phase_limit=system_settings.phase_limit)

    # determine half of clock's period
    half_period = int(1 / system_settings.desired_clk_freq * 1e9 / 2)
    if half_period == 0:
        raise RuntimeWarning("Invalid value of clock frequency provided")

    @always(delay(half_period))
    def drive_clk():
        clk.next = not clk

    @instance
    def stimulus():
        reset.next = 1
        yield clk.posedge
        reset.next = 0

        for i in range(periods * system_settings.phase_limit):
            yield clk.posedge
            results.append(int(output))

        raise StopSimulation

    return DUT, drive_clk, stimulus
