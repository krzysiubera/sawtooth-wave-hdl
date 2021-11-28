from myhdl import always, delay, StopSimulation, instance, Signal, intbv, block
from sawtooth_signal import generate_sawtooth_signal


@block
def generate_sawtooth_signal_testbench(system_settings):

    # declare signals
    output = Signal(intbv(0)[system_settings.bit_width:])
    clk = Signal(bool(0))
    reset = Signal(bool(0))

    # instantiate DUT
    DUT = generate_sawtooth_signal(output=output, clk=clk, reset=reset, bit_width=system_settings.bit_width,
                                   phase_limit=system_settings.phase_limit)

    @always(delay(1))
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
