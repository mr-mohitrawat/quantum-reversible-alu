from qiskit import QuantumCircuit

# AND Gate
def and_gate():
    qc = QuantumCircuit(3, name="AND Gate")
    qc.ccx(0, 1, 2)
    return qc