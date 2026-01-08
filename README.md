# qiskit-pharmaceutical-vqe

[![Tests](https://github.com/BrandonButera/qiskit-pharmaceutical-vqe/actions/workflows/tests.yml/badge.svg)](https://github.com/BrandonButera/qiskit-pharmaceutical-vqe/actions)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Quantum VQE algorithms for pharmaceutical drug discovery using IBM Quantum hardware and Qiskit.

## Overview

`qiskit-pharmaceutical-vqe` is a comprehensive Python package that leverages quantum computing to solve problems in pharmaceutical drug discovery. It provides implementations of Variational Quantum Eigensolver (VQE) algorithms optimized for molecular simulations, enabling researchers to compute ground state energies, molecular properties, and binding affinities using quantum computers.

### Key Features

- **Variational Quantum Eigensolver (VQE)** - State-of-the-art quantum algorithm for computing ground state energies
- - **Molecular Simulator** - Prepare quantum circuits and calculate molecular properties
  - - **Pharmaceutical Focus** - Optimized for drug discovery applications
    - - **IBM Quantum Integration** - Direct support for IBM Quantum hardware via Qiskit
      - - **Type Hints & Documentation** - Fully typed codebase with comprehensive docstrings
        - - **Comprehensive Testing** - Extensive test suite with high coverage
          - - **Production Ready** - Professional packaging, CI/CD, and quality assurance
           
            - ## Installation
           
            - ### From PyPI (Coming Soon)
           
            - ```bash
              pip install qiskit-pharmaceutical-vqe
              ```

              ### From Source

              Clone the repository and install in development mode:

              ```bash
              git clone https://github.com/BrandonButera/qiskit-pharmaceutical-vqe.git
              cd qiskit-pharmaceutical-vqe
              pip install -e .
              ```

              ### Install Development Dependencies

              For development and testing:

              ```bash
              pip install -e ".[dev]"
              ```

              For Jupyter notebook examples:

              ```bash
              pip install -e ".[jupyter]"
              ```

              ## Quick Start

              Here's a simple example to get started:

              ```python
              from pharma_vqe import VQEAlgorithm, MolecularSimulator
              from pharma_vqe.molecular_simulator import MoleculeType

              # Initialize molecular simulator for H2 molecule
              simulator = MolecularSimulator(molecule_type=MoleculeType.H2)

              # Get circuit requirements
              num_qubits = simulator.get_vqe_circuit_qubits()

              # Initialize VQE algorithm
              vqe = VQEAlgorithm(num_qubits=num_qubits, num_layers=1)

              # Prepare initial parameters
              initial_params = simulator.prepare_quantum_circuit_params()

              # Run VQE optimization
              optimized_params, min_energy = vqe.optimize(initial_params)

              # Calculate molecular properties
              properties = simulator.calculate_properties_from_energy(min_energy)
              print(f"Ground State Energy: {properties['ground_state_energy']:.6f} Hartree")
              print(f"Binding Affinity: {properties['binding_affinity']:.2f} kcal/mol")
              ```

              For more examples, see the [examples/](examples/) directory.

              ## Usage Guide

              ### Basic Workflow

              1. **Create a Molecular Simulator** - Initialize for your target molecule
              2. 2. **Set Up VQE Algorithm** - Configure quantum circuit parameters
                 3. 3. **Prepare Parameters** - Initialize circuit rotation angles
                    4. 4. **Optimize** - Run the VQE optimization loop
                       5. 5. **Analyze Results** - Calculate properties and validate results
                         
                          6. ### API Documentation
                         
                          7. #### VQEAlgorithm
                         
                          8. The main class for quantum variational eigensolver implementation.
                         
                          9. ```python
                             from pharma_vqe import VQEAlgorithm

                             vqe = VQEAlgorithm(num_qubits=4, num_layers=2)
                             optimized_params, min_energy = vqe.optimize(initial_parameters)
                             iterations = vqe.get_iteration_count()
                             ```

                             **Parameters:**
                             - `num_qubits` (int): Number of qubits in the quantum circuit
                             - - `num_layers` (int): Number of ansatz layers
                              
                               - **Methods:**
                               - - `optimize(initial_params)` - Run VQE optimization
                                 - - `get_iteration_count()` - Get number of iterations performed
                                  
                                   - #### MolecularSimulator
                                  
                                   - Handles molecular property calculations and quantum circuit preparation.
                                  
                                   - ```python
                                     from pharma_vqe import MolecularSimulator
                                     from pharma_vqe.molecular_simulator import MoleculeType

                                     simulator = MolecularSimulator(molecule_type=MoleculeType.H2)
                                     info = simulator.get_molecular_info()
                                     num_qubits = simulator.get_vqe_circuit_qubits()
                                     params = simulator.prepare_quantum_circuit_params()
                                     properties = simulator.calculate_properties_from_energy(energy)
                                     ```

                                     **Supported Molecules:**
                                     - H2 (Hydrogen)
                                     - - More coming soon...
                                      
                                       - **Methods:**
                                       - - `get_molecular_info()` - Get molecule description
                                         - - `get_vqe_circuit_qubits()` - Get required number of qubits
                                           - - `prepare_quantum_circuit_params()` - Initialize circuit parameters
                                             - - `calculate_properties_from_energy(energy)` - Compute molecular properties
                                               - - `validate_vqe_result(energy)` - Validate optimization results
                                                 - - `estimate_convergence_iterations()` - Estimate convergence time
                                                  
                                                   - ## Testing
                                                  
                                                   - Run the comprehensive test suite:
                                                  
                                                   - ```bash
                                                     pytest
                                                     pytest --cov=pharma_vqe  # With coverage report
                                                     ```

                                                     Individual test files:
                                                     - `tests/test_vqe_algorithm.py` - VQE algorithm tests
                                                     - - `tests/test_molecular_simulator.py` - Molecular simulator tests
                                                      
                                                       - ## Project Structure
                                                      
                                                       - ```
                                                         qiskit-pharmaceutical-vqe/
                                                         ├── pharma_vqe/              # Main package
                                                         │   ├── __init__.py
                                                         │   ├── vqe_algorithm.py    # VQE implementation
                                                         │   └── molecular_simulator.py  # Molecular simulator
                                                         ├── tests/                   # Test suite
                                                         │   ├── __init__.py
                                                         │   ├── test_vqe_algorithm.py
                                                         │   └── test_molecular_simulator.py
                                                         ├── examples/                # Usage examples
                                                         │   └── basic_usage.py
                                                         ├── docs/                    # Documentation
                                                         ├── pyproject.toml           # Modern Python packaging
                                                         ├── README.md                # This file
                                                         ├── CHANGELOG.md             # Version history
                                                         ├── CONTRIBUTING.md          # Contribution guidelines
                                                         └── LICENSE                  # Apache 2.0 license
                                                         ```

                                                         ## Contributing

                                                         We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
                                                         - Setting up the development environment
                                                         - - Making changes and running tests
                                                           - - Code style and formatting
                                                             - - Submitting pull requests
                                                              
                                                               - ## Requirements
                                                              
                                                               - - Python 3.8 or higher
                                                                 - - Qiskit >= 0.43.0
                                                                   - - IBM Quantum Runtime >= 0.15.0
                                                                     - - NumPy, SciPy, and other dependencies (see [requirements.txt](requirements.txt))
                                                                      
                                                                       - ## License
                                                                      
                                                                       - This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
                                                                      
                                                                       - ## Citation
                                                                      
                                                                       - If you use this package in your research, please cite:
                                                                      
                                                                       - ```bibtex
                                                                         @software{qiskit_pharma_vqe,
                                                                           title = {Quantum VQE for Pharmaceutical Applications},
                                                                           author = {Quantum Molecular Simulation Services},
                                                                           year = {2026},
                                                                           url = {https://github.com/BrandonButera/qiskit-pharmaceutical-vqe}
                                                                         }
                                                                         ```

                                                                         ## Acknowledgments

                                                                         Built with:
                                                                         - [Qiskit](https://qiskit.org/) - IBM's quantum computing framework
                                                                         - - [IBM Quantum](https://quantum.ibm.com/) - Quantum hardware access
                                                                           - - [OpenFermion](https://github.com/quantumlib/OpenFermion) - Quantum chemistry simulation
                                                                             - - [Mitiq](https://github.com/unitaryfund/mitiq) - Error mitigation toolkit
                                                                              
                                                                               - ## Support
                                                                              
                                                                               - For issues, questions, or feature requests:
                                                                               - - Open an [issue](https://github.com/BrandonButera/qiskit-pharmaceutical-vqe/issues)
                                                                                 - - Check existing [documentation](docs/)
                                                                                   - - Review [examples](examples/)
                                                                                    
                                                                                     - ## Roadmap
                                                                                    
                                                                                     - - [ ] Support for more molecules (LiH, H2O, etc.)
                                                                                       - [ ] - [ ] GPU acceleration for classical optimization
                                                                                       - [ ] - [ ] Noise-aware circuit optimization
                                                                                       - [ ] - [ ] Integration with popular QC hardware providers
                                                                                       - [ ] - [ ] Advanced error mitigation techniques
                                                                                       - [ ] - [ ] Interactive Jupyter tutorials
                                                                                      
                                                                                       - [ ] ---
                                                                                      
                                                                                       - [ ] **Last Updated:** January 7, 2026
                                                                                       - [ ] **Status:** Active Development
                                                                                       - [ ] 
