"""Print model 'training' for a while."""
import time
import numpy as np

error = 1.0
for i in np.arange(600):
    nudge = 0.1*np.random.rand()
    roll = np.random.rand() 
    if roll > 0.51:
        error += nudge
    elif roll > 0.49:
        with open('examples/fw_output.txt','a') as of:
            of.write('Unexpected error!\n')
    else:
        error -= nudge
    msg = f'Model training... Error: {error:.2f}\n'
    with open('examples/fw_output.txt','a') as of:
        of.write(msg)
    time.sleep(1)

