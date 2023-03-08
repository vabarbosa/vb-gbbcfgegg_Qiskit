from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer

qc_output = QuantumCircuit(2)
qc_output.h(0)
qc_output.cx(0, 1)

circuit_drawer(qc_output, initial_state=True, output='mpl').savefig('./pics/circuit.png')
