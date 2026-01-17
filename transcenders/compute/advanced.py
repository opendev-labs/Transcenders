from typing import List, Dict, Any
import pennylane as qml
import numpy as np

class AdvancedCircuit:
    def __init__(self, wires: int):
        self.wires = wires
        self.dev = qml.device("default.qubit", wires=wires)

    def execute(self, gates: List[Dict[str, Any]]):
        """
        Executes a dynamic circuit defined by a list of gate dictionaries.
        Format: {"gate": "Hadamard", "wires": [0], "params": []}
        """
        @qml.qnode(self.dev)
        def circuit():
            for g in gates:
                name = g.get("gate")
                w = g.get("wires")
                p = g.get("params", [])

                if name == "Hadamard":
                    qml.Hadamard(wires=w[0])
                elif name == "PauliX":
                    qml.PauliX(wires=w[0])
                elif name == "CNOT":
                    qml.CNOT(wires=w)
                elif name == "RX":
                    qml.RX(p[0], wires=w[0])
                elif name == "RY":
                    qml.RY(p[0], wires=w[0])
                elif name == "RZ":
                    qml.RZ(p[0], wires=w[0])
            
            # Measurement: Return probability distribution
            return qml.probs(wires=range(self.wires))

        return circuit().tolist()
