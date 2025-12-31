from qiskit import QuantumCircuit

# XOR Gate
def xor_gate():
    qc = QuantumCircuit(3, name="XOR Gate")
    qc.cx(0, 2)
    qc.cx(1, 2)
    return qc