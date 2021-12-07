from sawtooth_signal_tb import sawtooth_tb
from system_settings import SystemSettings


system_settings = SystemSettings(desired_clk_freq=0.5*1e9, bit_width=16, desired_wave_freq=1/1000e-9)
tb = sawtooth_tb(system_settings, periods=4)
tb.config_sim(trace=True)
tb.run_sim()
