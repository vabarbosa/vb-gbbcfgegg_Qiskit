#Flip the first qbit in the following string (00000000) to a 1 so that the result is: 10000000
from qiskit import QuantumCircuit, Aer
from qiskit.visualization import circuit_drawer, plot_histogram
import matplotlib.pyplot as plt

#Solution:
#1. create a quantum circuit of 8 qbits
qc_encode = QuantumCircuit(8)
#2. use the Pauli-X(X) gate to flip the first qbit from 0 to 1.
#info: In Quantum computing the Pauli-X(X) gate is the logical NOT gate for classical computers
#string:   00000000
#indexes:  01234567
qc_encode.x(7) # even if you'd expect the output to be 00000001, Qiskit numbers the bits on a string from right to left
#output: would be 10000000
#let's create an object image before measurements
qc_encode.draw()
circuit_drawer(qc_encode, initial_state=True, output='mpl').savefig('./pics/before_measurement.png')
#measures the qubit states(in our case either 0 or 1) and saves them to classical bits
qc_encode.measure_all()
#let's create an object image after the measurements
qc_encode.draw()
circuit_drawer(qc_encode, initial_state=True, output='mpl').savefig('./pics/after_measurement.png')

#load the quantum simulator
sim = Aer.get_backend('aer_simulator')
#run the simulator on the qc_encode and get the results
result = sim.run(qc_encode).result()
#get the binary equivalent of each qbit
counts = result.get_counts()

#the output of the print below should be {'10000000': 1024} which means that there were 1024 shots (how many times the
 #quantum circuit was run) and there were 1024 counts (how many times this result '10000000' was found).
print(counts)

#create a histogram object
plot_histogram(counts)



plt.savefig('./pics/histogram.png', bbox_inches='tight', pad_inches=1)