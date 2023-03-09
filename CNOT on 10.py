from qiskit import QuantumCircuit, Aer
from qiskit.visualization import circuit_drawer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# create a quantum circuit with 2 qbits and 2 cbits
qc = QuantumCircuit(2,2)

# flip the first qbit
qc.x(0)
qc.draw()
circuit_drawer(qc, initial_state=True, output='mpl').savefig('./pics/bm_cnot.png')


# apply CNOT to both qbits
qc.cx(0,1)
qc.draw()
circuit_drawer(qc, initial_state=True, output='mpl').savefig('./pics/in_cnot.png')

qc.measure(0,0)
qc.measure(1,1)
qc.draw()
circuit_drawer(qc, initial_state=True, output='mpl').savefig('./pics/am_cnot.png')