from myhdl import block, Signal, intbv, always_seq, always_comb


@block
def generate_sawtooth_signal(output: Signal, clk: Signal, reset: Signal, bit_width: int, phase_limit: int):
    """
    Architecture of block generating sawtooth signal
    Args:
        output: (Signal) - output signal with sawtooth wave generated
        clk: (Signal) - system clock signal
        reset: (Signal) - reset signal
        bit_width: (int) - parameter from SystemSettings class - maximum bit width of the signal
        phase_limit: (int) - parameter from SystemSettings class needed to determine behaviour of the block

    Yields:
        logic: describing behaviour of the block
    """

    # counter for phase
    phase_counter = Signal(intbv(0)[bit_width:])

    @always_seq(clk.posedge, reset=reset)
    def logic():

        if reset == 1:
            phase_counter.next = 0
        else:
            if phase_counter == phase_limit - 1:
                phase_counter.next = 0
            else:
                phase_counter.next = phase_counter + 1

    @always_comb
    def comb_logic():
        output.next = phase_counter

    return logic, comb_logic
