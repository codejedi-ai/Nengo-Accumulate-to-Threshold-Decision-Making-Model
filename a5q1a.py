import nengo
# import matplotlib.pyplot as plt
# 
# Create the model
model = nengo.Network()
with model:
    # Create an ensemble with 50 neurons
    accum = nengo.Ensemble(n_neurons=50, dimensions=1)
    # acc.noise = nengo.processes.WhiteSignal(period=10, high=100, rms=1)
    # Create an input node with a constant value of 0.1
    input_node = nengo.Node(output=[0.1])

    # Connect the input node to the ensemble
    nengo.Connection(input_node, accum)

    # Connect the ensemble back to itself with a synapse of 0.1
    nengo.Connection(accum, accum, synapse=0.1)

    # Create a probe to record the value stored in the ensemble
    probe = nengo.Probe(accum, synapse=0.01)
    output_probe = nengo.Node(size_in=1)

    nengo.Connection(accum, output_probe)
# Run the model for 2 seconds for each input
inputs = [0.2, 0.1, -0.1, -0.2]
for input_val in inputs:
    with nengo.Simulator(model) as sim:
        # Set the input node to the current input value
        input_node.output = [input_val]

        # Run the simulation for 2 seconds
        sim.run(2)

        # Plot the value stored in the accumulator
        plt.plot(sim.trange(), sim.data[probe], label=f"Input: {input_val}")

# Add labels and legend to the plot
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Accumulator System")
plt.legend()

# Show the plot
plt.show()
