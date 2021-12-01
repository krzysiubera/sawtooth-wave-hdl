from sawtooth_signal_tb import sawtooth_tb
from system_settings import SystemSettings


system_settings = SystemSettings()
tb = sawtooth_tb(system_settings)
tb.config_sim(trace=True)
tb.run_sim()

