from qiskit import QuantumCircuit, Aer
from qiskit.visualization import circuit_drawer, plot_histogram
import matplotlib.pyplot as plt

#output age 88

qc_encode = QuantumCircuit(7)


qc_encode.x(6)
qc_encode.x(4)
qc_encode.x(3)


qc_encode.draw()  # this drawing will show where the gates are placed
circuit_drawer(qc_encode, initial_state=True, output='mpl').savefig('./pics/before_measurement_age.png')


qc_encode.measure_all()
qc_encode.draw()  # this drawing will apply the gates to the qbits
circuit_drawer(qc_encode, initial_state=True, output='mpl').savefig('./pics/after_measurement_age.png')


sim = Aer.get_backend('aer_simulator')
result = sim.run(qc_encode).result()
counts = result.get_counts()
print(counts)  # this print will output the equivalent in classical bits of the qbits


plot_histogram(counts)
plt.savefig('./pics/histogram_age.png', bbox_inches='tight', pad_inches=1)