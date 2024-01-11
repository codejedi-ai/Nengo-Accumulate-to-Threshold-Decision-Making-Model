import nengo
import numpy as np
def choice(x):
    if x[0] > 0.9:
        return 1
    elif x[0] < -0.9:
        return -1
    else:
        return 0

# Create the model
model = nengo.Network()
with model:
    # Create an ensemble with 50 neurons
    accum = nengo.Ensemble(n_neurons=100, dimensions=2, radius = np.sqrt(2))
    
    # Create an input node with a constant value of 0.1
    input_node = nengo.Node(output=[0])
    # Add white noise to the accumulator
    white_noise = nengo.processes.WhiteSignal(period=10, high=100, rms=1)
    accum.noise = white_noise
    # Connect the input node to the ensemble
    nengo.Connection(input_node, accum[0])

    # Connect the ensemble back to itself with a synapse of 0.1
    nengo.Connection(accum[0], accum[0], synapse=0.1)
    nengo.Connection(accum[0], accum[1], function = choice)
    # Create a probe to record the value stored in the ensemble
    
    gui_probe = nengo.Node(size_in=1)
    nengo.Connection(accum[1], gui_probe)
    integrator_probe = nengo.Node(size_in=1)
    nengo.Connection(accum[0], integrator_probe)
    
    # probes
    probe = nengo.Probe(accum[1], synapse=0.01)