#--------Your first quantum circuit

#Install Qiskit
from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# Create the circuit
qc_output = QuantumCircuit(8)
qc_output.measure_all()
qc_output.draw(initial_state=True)


sim = Aer.get_backend('aer_simulator')
result = sim.run(qc_output).result()
counts = result.get_counts()
plot_histogram(counts)

# Save the histogram to a PNG file
plt.savefig('./pics/histogram.png')