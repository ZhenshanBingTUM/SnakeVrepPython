README

Note 1: Since the integrator constantly sums its input, it will saturate quickly if you leave the input non-zero.

Step 1: Create the neural populations
Step 2: Create input for the model
        We will use a piecewise step function as input, so we can see the effects of recurrence.
        from nengo.utils.functions import piecewise
Step 3: Connect the network elements
          1). Connect the pupulation to itself
          2). Connect the input
Step 4: Probe outputs
        Anything that is probed will collect the data it produces over time, allowing us to analyze and visualize it later
Step 5: Run the model
