from qiskit import QuantumCircuit, Aer
from qiskit.visualization import circuit_drawer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

#our qbits are (0,0)
qc_cnot = QuantumCircuit(2)  # create a qcircuit with 2 qbits

#perform a CNOT: flip both qbits if the target qbits is 1 (the first qbit: the qbit at index 0; the second qbit: the qbit at index 1)
qc_cnot.cx(0,1)  # the 0 and 1 in the parentheses are the index of the quantum qbits
qc_cnot.draw()
circuit_drawer(qc_cnot, initial_state=True, output='mpl').savefig('./pics/bm_adding_with_qiskit.png')

qc_cnot.measure_all()
circuit_drawer(qc_cnot, initial_state=True, output='mpl').savefig('./pics/am_adding_with_qiskit.png')

sim = Aer.get_backend('aer_simulator')
result = sim.run(qc_cnot).result()
counts = result.get_counts()
plot_histogram(counts)

plt.savefig('./pics/adding_with_qiskit_histogram.png')
