from myhdl import always, delay, StopSimulation, instance, Signal, intbv, block
from sawtooth_signal import generate_sawtooth_signal
from system_settings import SystemSettings


@block
def sawtooth_tb(system_settings: SystemSettings):
    """
    Test bench for sawtooth wave generator
    Args:
        system_settings: (SystemSettings) - settings for the system encapsulated in the class

    Yields:
        DUT: instance of the tested device
        drive_clk: process driving clock
        stimulus: process driving the application
    """

    # declare signals
    output = Signal(intbv(0)[system_settings.bit_width:])
    clk = Signal(bool(0))
    reset = Signal(bool(0))

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
        for i in range(8 * system_settings.phase_limit):
            yield clk.posedge

        for i in range(4):
            if i < 2:
                reset.next = True
            else:
                reset.next = False
            yield clk.posedge

        raise StopSimulation

    return DUT, drive_clk, stimulus
