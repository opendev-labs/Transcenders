# Transcenders

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()

> The unified unified CLI and SDK for the **opendev-labs** quantum ecosystem.

## 🚀 Overview

**Transcenders** is the flagship integration tool that unifies **Quantum-ML**, **Quantum-API**, and **Quantum-Compute** into a single, cohesive experience. It provides a powerful Command Line Interface (CLI) and a streamlined Python SDK for developers to build, deploy, and manage entire quantum workflows.

## ✨ Key Features

- **Unified CLI**: Manage API services, compute jobs, and ML training from a single tool.
- **Ecosystem Integration**: Native support for all **opendev-labs** libraries.
- **Workflow Automation**: Scripts and utilities to automate deployment and testing.
- **Developer First**: Rich autocompletion and help commands.

## 🛠️ Installation

```bash
pip install .
```

## 💻 Usage

### CLI

```bash
# Check system status
transcenders api status

# Submit a job
transcenders compute submit --file circuit.qasm

# Train a model
transcenders ml train --config config.yaml
```

### Python SDK

```python
import transcenders

# Initialize the ecosystem
env = transcenders.Environment()

# Access specific modules
api = env.api
compute = env.compute

print(f"Connected to {api.endpoint}")
```

## 🤝 Contributing

We are building the future of easy-to-use quantum tools. Join us!

1. Fork the repo: `https://github.com/opendev-labs/Transcenders`
2. Create your branch.
3. Submit a PR.

## 📄 License

This project is licensed under the MIT License.

---
Copyright © 2026 **opendev-labs**
