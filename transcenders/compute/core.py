import pennylane as qml

class QuantumDevice:
    """
    Wrapper for Quantum Devices in TRANSCENDERS.
    """
    def __init__(self, wires=3, backend="default.qubit"):
        self.wires = wires
        self.backend = backend
        self.device = qml.device(backend, wires=wires)

    def get_device(self):
        return self.device
