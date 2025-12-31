from qiskit import QuantumCircuit
from gates.and_gate import and_gate
from gates.xor_gate import xor_gate

def full_adder():
    qc = QuantumCircuit(5, name="Full Adder")
    qc.append(xor_gate().to_gate(), [0, 1, 3])
    qc.append(and_gate().to_gate(), [0, 1, 4])
    qc.ccx(2, 3, 4)
    qc.cx(2, 3)
    return qc