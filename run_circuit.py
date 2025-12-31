from qiskit import transpile
from qiskit_aer import Aer
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit_ibm_runtime.fake_provider import FakeFez
from qiskit_ibm_runtime import QiskitRuntimeService


aer_backend = Aer.get_backend('qasm_simulator')
ibm_fake_backend = FakeFez()
ibm_quantum_backend = QiskitRuntimeService().least_busy(simulator=False, operational=True)

# Run on Aer Simulator
def aer_simulator(qc, shots):
    qc_t = transpile(qc, aer_backend)
    result = aer_backend.run(qc_t, shots=shots).result()
    count = result.get_counts()
    print("Aer Simulator Measurement Result: ", count)

def ibm_fake_simulator(qc, shots):
    qc_t = transpile(qc, backend=ibm_fake_backend)
    sampler = Sampler(mode=ibm_fake_backend)
    job = sampler.run([qc_t], shots=shots)
    result = job.result()

    pub_result = result[0]
    reg_name = list(pub_result.data.keys())[0]
    bit_array = pub_result.data[reg_name]

    counts = bit_array.get_counts()
    print("IBM Fake Simulator Measurement Result: ", counts)

def ibm_quantum_hardware(qc, shots):
    qc_t = transpile(qc, backend=ibm_quantum_backend)
    sampler = Sampler(mode=ibm_quantum_backend)
    job = sampler.run([qc_t], shots=shots)
    result = job.result()

    pub_result = result[0]
    reg_name = list(pub_result.data.keys())[0]
    bit_array = pub_result.data[reg_name]

    counts = bit_array.get_counts()
    print("IBM Quantum Hardware Measurement Result: ", counts)