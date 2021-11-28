from myhdl import block, Signal, intbv, always


@block
def generate_sawtooth_signal(output, clk, reset, bit_width, phase_limit):
    """
    output - sawtooth signal
    clk - clock signal
    reset - reset signal
    bit_width - maximum bit width
    phase_limit - limit of phase
    """

    # counter for phase
    phase_counter = Signal(intbv(0)[bit_width:])

    @always(clk.posedge)
    def logic():

        if reset == 1:
            phase_counter.next = 0
            output.next = 0
        else:
            if phase_counter == phase_limit - 1:
                phase_counter.next = 0
                output.next = 0
            else:
                output.next = output + 1
                phase_counter.next = phase_counter + 1

    return logic
