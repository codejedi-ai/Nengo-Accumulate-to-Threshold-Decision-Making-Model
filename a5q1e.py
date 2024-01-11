import nengo
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
    accum = nengo.Ensemble(n_neurons=50, dimensions=1)
    output = nengo.Ensemble(n_neurons=50, dimensions=1)
    
    # Create an input node with a constant value of 0.1
    input_node = nengo.Node(output=[0])
    # Add white noise to the accumulator
    white_noise = nengo.processes.WhiteSignal(period=10, high=100, rms=1)
    accum.noise = white_noise
    # Connect the input node to the ensemble
    nengo.Connection(input_node, accum)

    # Connect the ensemble back to itself with a synapse of 0.1
    nengo.Connection(accum, accum, synapse=0.1)
    nengo.Connection(accum, output, function = choice)
    # Create a probe to record the value stored in the ensemble
    probe = nengo.Probe(output, synapse=0.01)