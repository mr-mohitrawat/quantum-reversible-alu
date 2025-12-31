from qiskit import QuantumCircuit

def mux_4_x_1():
    qc = QuantumCircuit(8, name="Mux 4 X 1")

    # 0 0
    qc.x(0); qc.x(1)
    qc.ccx(0, 1, 6)
    qc.ccx(6, 2, 7)
    qc.ccx(0, 1, 6)
    qc.x(0); qc.x(1)

    # 0 1
    qc.x(0)
    qc.ccx(0, 1, 6)
    qc.ccx(6, 3, 7)
    qc.ccx(0, 1, 6)
    qc.x(0)

    # 1 0
    qc.x(1)
    qc.ccx(0, 1, 6)
    qc.ccx(6, 4, 7)
    qc.ccx(0, 1, 6)
    qc.x(1)

    # 1 1
    qc.ccx(0, 1, 6)
    qc.ccx(6, 5, 7)
    qc.ccx(0, 1, 6)

    return qc