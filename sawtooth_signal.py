from myhdl import block, Signal, intbv, always_seq, always_comb, ResetSignal


@block
def generate_sawtooth_signal(output: Signal, clk: Signal, reset: ResetSignal, bit_width: int, phase_limit: int):
    """
    Architecture of block generating sawtooth signal
    Args:
        output: (Signal) - output signal with sawtooth wave generated
        clk: (Signal) - system clock signal
        reset: (ResetSignal) - reset signal
        bit_width: (int) - parameter from SystemSettings class - maximum bit width of the signal
        phase_limit: (int) - parameter from SystemSettings class needed to determine behaviour of the block

    Yields:
        seq_logic: sequential logic of the design
        comb_logic: combination logic of the design
    """

    # counter for phase
    phase_counter = Signal(intbv(0)[bit_width:])

    @always_seq(clk.posedge, reset=reset)
    def seq_logic():

        if reset.active:
            phase_counter.next = 0
        else:
            if phase_counter == phase_limit - 1:
                phase_counter.next = 0
            else:
                phase_counter.next = phase_counter + 1

    @always_comb
    def comb_logic():
        output.next = phase_counter

    return seq_logic, comb_logic
