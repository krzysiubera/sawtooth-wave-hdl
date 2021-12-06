Generator of sawtooth wave written using myhdl package and converted to VHDL. Structure of files:
- sawtooth_signal.py - architecture of the block generating sawtooth signal
- sawtooth_signal_tb.py - test bench for the module
- system_settings.py - class containing settings for the system: clock frequency, output signal frequency, bit width of output signal
- unit_testing.py - tests for the module
- convert_to_hdl.py - code for converting design to HDL
- exceptions.py - custom exceptions
- run_tb.py - code for running the test bench
- hdl/ - result of conversion to HDL
