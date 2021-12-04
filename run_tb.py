from sawtooth_signal_tb import sawtooth_tb, results
from system_settings import SystemSettings


system_settings = SystemSettings()
tb = sawtooth_tb(system_settings, periods=8)
tb.config_sim(trace=True)
tb.run_sim()
print(results)

