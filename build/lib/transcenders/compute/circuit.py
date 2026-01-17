import pennylane as qml
from .core import QuantumDevice

class QuantumCircuit:
    """
    Base class for defining Quantum Circuits in TRANSCENDERS.
    """
    def __init__(self, device: QuantumDevice):
        self.q_device = device
        self.dev = device.get_device()

    def create_circuit(self):
        """
        Returns a QNode. Subclasses or methods should define the operations.
        """
        @qml.qnode(self.dev)
        def circuit(inputs):
            qml.Hadamard(wires=0)
            qml.RX(inputs[0], wires=0)
            qml.RY(inputs[1], wires=1)
            qml.CNOT(wires=[0, 1])
            qml.CNOT(wires=[1, 2])
            return qml.expval(qml.PauliZ(0))
        
        return circuit

    def run(self, inputs):
        """
        Executes the circuit with given inputs.
        """
        c = self.create_circuit()
        return c(inputs)
