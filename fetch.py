import numpy as np
import matplotlib.pyplot as plt
from lecroy import LeCroyScope

scope = LeCroyScope(host="131.225.138.156")


nsequence = 10
scope.clear()
scope.set_sequence_mode(nsequence)
settings = scope.get_settings()
for a, b in settings.items():
    print(a, ":", b)

if b'ON' in settings['SEQUENCE']:
    sequence_count = int(settings['SEQUENCE'].split(b',')[1])
else:
    sequence_count = 1
    
if nsequence != sequence_count:
    print( 'Could not configure sequence mode properly')
if sequence_count != 1:
    print( 'Using sequence mode with %i traces per aquisition' % sequence_count)

scope.trigger()
desc, array = scope.get_waveform(2)
# wf = desc['vertical_gain']*array - desc['vertical_offset']
print("---------- Descritption of waveform ---------")
for a, b in desc.items():
    print(a, ":", b)

plt.plot(array)
plt.show()