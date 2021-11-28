from sawtooth_signal_tb import generate_sawtooth_signal_testbench
from system_settings import SystemSettings


system_settings = SystemSettings()
tb = generate_sawtooth_signal_testbench(system_settings)
tb.config_sim(trace=True)
tb.run_sim()

