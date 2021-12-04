from myhdl import Signal, ResetSignal, intbv
from sawtooth_signal import generate_sawtooth_signal
from system_settings import SystemSettings


# instantiate system settings
system_settings = SystemSettings()

# declare signals
output = Signal(intbv(0)[system_settings.bit_width:])
clk = Signal(bool(0))
reset = ResetSignal(1, active=1, isasync=False)

# instantiate device
dut = generate_sawtooth_signal(output=output, clk=clk, reset=reset, bit_width=system_settings.bit_width,
                               phase_limit=system_settings.phase_limit)

# convert to HDL
dut.convert(hdl='VHDL', initial_values=True)
