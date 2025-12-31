from qiskit import QuantumCircuit

# OR Gate
def or_gate():
    qc = QuantumCircuit(3, name="OR Gate")
    qc.x(0)
    qc.x(1)
    qc.ccx(0, 1, 2)
    qc.x(2)
    qc.x(0)
    qc.x(1)
    return qc