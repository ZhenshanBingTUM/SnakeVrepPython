#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 22:21:34 2016

@author: zhenshan
""" 

import nengo
import numpy as np
import matplotlib.pyplot as plt

model = nengo.Network()
with model:

	x = nengo.Ensemble(n_neurons = 400, dimensions = 2)

	synapse = 0.1 # the smaller, the faster to response

	def vdp(x):
		omega = 0.4*np.pi
		b = 4
		return [synapse * (x[0] * (1 - b*x[1]**2) * 0.1 - omega**2 * x[1]) + x[0],
			    synapse * x[0] + x[1]]



#xdot(1) = x(1) * (1 - b*x(2)^2)*0.1 - w0^2*x(2);
#xdot(2) = x(1);

# best parameter synpase = 0.1, n_neurons = 200
#                synpase = 0.05, n_neurons = 400

# ## Step 2: Provide Input to the Model
# A brief input signal is provided to trigger the oscillatory behavior of the neural representation.
from nengo.utils.functions import piecewise
with model:
    # Create an input signal
    input = nengo.Node(piecewise({0: [1, 0], 0.1: [0, 0]}))
    #input = nengo.Node(piecewise({0.1, 0.1}))
    
    # Connect the input signal to the neural ensemble
    nengo.Connection(input, x)
    
    # Create the feedback connection
    nengo.Connection(x, x, synapse = synapse, function = vdp)

with model:
#    input_probe = nengo.Probe(input, 'output')
    neuron_probe = nengo.Probe(x, 'decoded_output', synapse=0.1)

# Create the simulator
with nengo.Simulator(model) as sim:
    # Run it for 5 seconds
    sim.run(20)

plt.plot(sim.trange(), sim.data[neuron_probe])
plt.xlabel('Time (s)', fontsize='large')
plt.legend(['$x_0$', '$x_1$']);
