# Qiskit Pharmaceutical VQE Documentation

Welcome to the documentation for the Qiskit Pharmaceutical VQE package!

## Table of Contents

1. [Getting Started](getting-started.md)
2. [API Reference](api-reference.md)
3. [Tutorials](tutorials/)
4. [Examples](../examples/)

## Quick Links

- [Installation Guide](getting-started.md#installation)
- [Quick Start Tutorial](getting-started.md#quick-start)
- [VQEAlgorithm API](api-reference.md#vqealgorithm)
- [MolecularSimulator API](api-reference.md#molecularsimulator)

## Overview

The `qiskit-pharmaceutical-vqe` package provides quantum computing tools for pharmaceutical drug discovery, specifically implementing Variational Quantum Eigensolver (VQE) algorithms optimized for molecular simulations.

### Key Features

- **VQE Algorithm**: State-of-the-art quantum algorithm for ground state energy calculations
- **Molecular Simulator**: Tools for molecular property calculations
- **IBM Quantum Integration**: Direct support for IBM Quantum hardware
- **Type-Safe**: Fully typed codebase with comprehensive documentation

## Contributing to Documentation

Documentation is written in Markdown and located in the `docs/` directory. To contribute:

1. Edit or create Markdown files
2. Follow the existing structure and style
3. Test your changes locally
4. Submit a pull request

## Building Documentation

To build the documentation locally with Sphinx:

```bash
pip install -e ".[dev]"
cd docs
make html
```

## Support

For questions or issues:
- [GitHub Issues](https://github.com/BrandonButera/qiskit-pharmaceutical-vqe/issues)
- [Examples](../examples/)
- [Contributing Guide](../CONTRIBUTING.md)
